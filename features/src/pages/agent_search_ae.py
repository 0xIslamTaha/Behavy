import time
from features.src.utility.basic_test import BaseTest


class AgentSearchAE(BaseTest):
    def __init__(self, context):
        self.driver = context.driver
        super().__init__(driver=self.driver)

    def count_agents(self):
        data = self.find_element('count_agents').text
        return int(data.split()[0])

    def filter_indian_agents(self):
        self.click('nationality')
        self.click('india')
        time.sleep(5)
