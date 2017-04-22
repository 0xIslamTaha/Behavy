from selenium import webdriver
import os
import time
from pyvirtualdisplay import Display

def before_all(context):
    context.base_url = {'qa': 'https://www.propertyfinder.qa/',
                        'ae': 'https://www.propertyfinder.ae/'}
    if not os.path.exists("reports"):
        os.makedirs("reports")
    os.chdir("reports")
    context.report_name = str(int(time.time()))
    print(" Before All\n", "Reports Dir: reports/%s" % context.report_name)
    os.makedirs(context.report_name)

def before_scenario(context, scenario):
    BROWSER = set_the_browser(context)
    fire_the_browser(context, BROWSER)

def after_scenario(context, scenario):
    print("  Scenario status: %s" % scenario.status)
    if scenario.status == "failed":
        take_screenshot(context, scenario)
    context.driver.quit()
    try:
        context.display.stop()
    except:
        pass

def set_the_browser(context):
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'

    return BROWSER

def fire_the_browser(context, BROWSER):
    if 'HEADLESS_MODE' in context.config.userdata.keys():
        if context.config.userdata['HEADLESS_MODE']:
            context.display = Display(visible=0, size=(1280, 790))
            context.display.start()

    if BROWSER == 'chrome':
        context.driver = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.driver = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.driver = webdriver.Safari()
    elif BROWSER == 'ie':
        context.driver = webdriver.Ie()
    elif BROWSER == 'opera':
        context.driver = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.driver = webdriver.PhantomJS()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    print("Before scenario\n")

def take_screenshot(context, scenario):
    if not os.path.exists("failed_scenarios_screenshots"):
        os.makedirs("failed_scenarios_screenshots")
    os.chdir("failed_scenarios_screenshots")
    context.driver.save_screenshot(scenario.name + "_failed.png")
    os.chdir('..')
