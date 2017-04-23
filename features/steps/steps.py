from behave import *
from features.src.pages.home_page_qa import HomePageQA
from features.src.pages.home_page_ae import HomePageAE
from features.src.pages.agent_page_ae import AgentPageAE
from features.src.pages.agent_search_ae import AgentSearchAE

@Given('I open https://www.propertyfinder.qa web site')
def step_impl(context):
    context.home_page_qa = HomePageQA(context)
    assert 'propertyfinder.qa' in context.driver.title

@when('I search for VILLA to BUY in location THE PEARL with minimum 3BEDS and maximum 7BEDS')
def step_impl(context):
    context.home_page_qa.buy_villa(location='The pearl',
                                min_beds=3,
                                max_beds=7)
    assert context.home_page_qa.element_is_exist('is_result')
    context.results_len = context.home_page_qa.count_results()

@step(u'Sort the villas from maximum price to lowest price')
def step_impl(context):
    context.home_page_qa.sort_results(by='price_high')

@step(u'Fetch all the prices of the listing and save it in a csv')
def step_impl(context):
    price_list = context.home_page_qa.get_results_info()
    context.price_list_len = len(price_list)
    context.home_page_qa.generate_reports(file_name='priceList.csv', data=price_list, path=context.report_name)

@Then('Make sure that the listing items are equal to the results')
def step_impl(context):
    assert context.results_len is context.price_list_len

@Given('I open https://www.propertyfinder.ae web site')
def step_impl(context):
    context.home_page_ae = HomePageAE(context)
    assert 'propertyfinder.ae' in context.driver.title

@when('I click on find agent tab')
def step_impl(context):
    assert context.home_page_ae.find_agent()

@step('Select the first agent')
def step_impl(context):
    context.home_page_ae.select_first_agent()

@step('Capture information about him in a text file')
def step_impl(context):
    context.agent_page_ae = AgentPageAE(context)
    info = context.agent_page_ae.get_agent_info()
    context.agent_page_ae.export_agent_info(info=info, path=context.report_name)

@step('Capture a screen shot')
def step_impl(context):
    context.agent_page_ae.take_screenshot(context.report_name)

@step('Change language to arabic')
def step_impl(context):
    context.agent_page_ae.change_lang_to_arabic()

@then('make sure that language changed to arabic then capture a screen shoot')
def step_impl(context):
    url = context.agent_page_ae.get_url()
    assert '/ar/' in url
    context.agent_page_ae.take_screenshot(context.report_name)

@step('Filter agents who can speak "HINDI, ENGLISH, ARABIC"')
def step_impl(context):
    langs = ['Hindi', 'English', 'Arabic']
    context.home_page_ae.filter_agent_by_lang(langs)

@step('Note down the total count of agents before')
def step_impl(context):
    context.agent_search_ae = AgentSearchAE(context)
    context.before = context.agent_search_ae.count_agents()

@step('Filter agents from India')
def step_impl(context):
    context.agent_search_ae.filter_indian_agents()

@step('Note down the total count of agents after')
def step_impl(context):
    context.after = context.agent_search_ae.count_agents()

@step('Assert that latest count is less than the previous count')
def step_impl(context):
    assert context.after < context.before
