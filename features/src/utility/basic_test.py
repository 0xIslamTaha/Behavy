from features.src.utility.elements import elements
import csv
import uuid
import time
from selenium.webdriver.common.by import By
import os


class BaseTest(object):
    def __init__(self, driver):
        self.driver = driver
        self.elements = elements

    def get_page(self, url):
        self.driver.get(url=url)

    def find_element(self, element):
        method = self.elements[element][0]
        value = self.elements[element][1]
        if method in ['XPATH', 'ID', 'LINK_TEXT']:
            element_value = self.driver.find_element(getattr(By, method), value)
        elif method in ['CLASS_NAME', 'NAME', 'TAG_NAME']:
            item_order = self.elements[element][2]
            elements_value = self.driver.find_elements(getattr(By, method), value)
            if item_order == -1:
                element_value = elements_value
            else:
                element_value = elements_value[item_order]
        return element_value

    def element_is_exist(self, element):
        self.firefox_wait()
        try:
            self.find_element(element=element)
            return True
        except:
            return False

    def get_attribute(self, element, attribute):
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        return self.find_element(element).text

    def take_screenshot(self, path):
        os.chdir(path)
        name = str(uuid.uuid4()).split('-')[0] + '.png'
        self.driver.save_screenshot(name)
        os.chdir('..')

    def click(self, element):
        for temp in range(10):
            try:
                self.find_element(element).click()
                break
            except:
                time.sleep(1)
        else:
            self.fail("can't find %s element" % element)
        time.sleep(1)

    def get_url(self):
        return self.driver.current_url

    def generate_reports(self, data, path, file_name='report.csv'):
        os.chdir(path)
        with open(file_name, 'w') as report:
            report_write = csv.writer(report, quoting=csv.QUOTE_ALL)
            report_write.writerow(['Title', 'Price'])
            for row in data:
                report_write.writerow(row)
        os.chdir('..')

    def export_agent_info(self, path, info):
        os.chdir(path)
        file_name = info[0][6:]
        with open(file_name, 'w') as report:
            for row in info:
                report.write(row)
                report.write('\n')
        os.chdir('..')

    def firefox_wait(self):
        # Hack to bypass this issue 'https://github.com/mozilla/geckodriver/issues/308'
        if self.driver.name == 'firefox':
            time.sleep(10)
