from features.src.utility.basic_test import BaseTest
import time


class HomePageQA(BaseTest):
    def __init__(self, context):
        base_url = context.base_url['qa']
        self.driver = context.driver
        super().__init__(driver=self.driver)
        if 'BASE_URL' in context.config.userdata.keys() and context.config.userdata['BASE_URL']  is not None:
            self.get_page(context.config.userdata['BASE_URL'])
        else:
            self.get_page(base_url)

    def buy_villa(self, location, min_beds, max_beds):
        search = self.find_element(element='search')
        if search.get_attribute('data-selected-section') != 'buy':
            self.click(element='action')
            self.click(element='select_buy')

        self.click(element='property_type')
        self.click(element='select_villa')

        self.click(element='min_beds_button')
        self.click(element='select_3_beds')

        self.click(element='max_beds_button')
        self.click(element='select_7_beds')

        city = self.find_element('city')
        city.clear()
        city.send_keys(location)
        city.submit()

    def sort_results(self, by):
        self.click(element='sort_results')
        self.click(element='price_high')
        self.firefox_wait()

    def get_results_info(self):
        data = []
        results_data_list = self.find_element('results_data_list')
        for result in results_data_list:
            title = result.find_element_by_tag_name('h2').text
            price = result.find_element_by_class_name('price').text
            data.append([title, price])
        return data

    def count_results(self):
        result = self.find_element('is_result').text.split()
        return int(result[0])