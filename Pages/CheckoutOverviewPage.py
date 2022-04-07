import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage


class CheckoutOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def checkout_overview_page_header(self):
        return self.get_element_text(Locators.CHECKOUT_OVERVIEW_PAGE_HEADER)

    def do_click_on_finish_button(self):
        print(self.driver.title)
        element= self.driver.find_element_by_xpath("//button[contains(text(),'Finish')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)