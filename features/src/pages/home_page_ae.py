from features.src.utility.basic_test import BaseTest

class HomePageAE(BaseTest):
    def __init__(self, context):
        base_url = context.base_url['ae']
        self.driver = context.driver
        super().__init__(driver=self.driver)
        if 'BASE_URL' in context.config.userdata.keys() and context.config.userdata['BASE_URL']  is not None:
            self.get_page(context.config.userdata['BASE_URL'])
        else:
            self.get_page(base_url)

    def find_agent(self):
        try:
            self.click('find_agent')
            return True
        except:
            return False

    def select_first_agent(self):
        self.firefox_wait()
        self.click('first_agent')

    def filter_agent_by_lang(self, langs):
        langs = set(langs)
        self.click('language')
        language_list = self.find_element('language_list').find_elements_by_tag_name('li')
        for language in language_list:
            if language.text in langs:
                language.click()
        self.find_element('search_form').submit()


