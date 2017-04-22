from features.src.utility.basic_test import BaseTest


class AgentPageAE(BaseTest):
    def __init__(self, context):
        self.driver = context.driver
        super().__init__(driver=self.driver)

    def get_agent_info(self):
        user_info = self.get_text('user_info')
        user_info_list = user_info.split('\n')

        user_personal_info = self.get_text('user_personal_info')
        user_personal_info_list = user_personal_info.split('\n')

        company_name = self.get_text('company_name')

        phone = self.get_attribute('call_agent', 'data-phone')

        self.click('about_me_button')
        about_me = self.get_text('about_me')

        user_linkedIn = ''
        try:
            user_linkedIn = self.get_attribute('view_profile', 'href')
        except:
            pass

        data = ['Name: %s' % user_info_list[0],
                'Nationality: %s' % user_info_list[3],
                'Languages: %s' % user_info_list[5],
                'License No: %s' % user_personal_info_list[2],
                'About Me: %s' % about_me,
                'Phone Number: %s' % phone,
                'Company Name: %s' % company_name,
                'Experience: %s' % user_personal_info_list[6],
                'No of active listings: %s' % user_info_list[7],
                ]

        if user_linkedIn:
            data.append('LinkedIn URL: %s' % user_linkedIn)

        return data

    def change_lang_to_arabic(self):
        if '/ar/' not in self.driver.current_url:
            self.click('arabic')
        self.firefox_wait()