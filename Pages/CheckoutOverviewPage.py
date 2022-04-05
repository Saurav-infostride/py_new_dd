import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage

class CheckoutOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def checkout_overview_page_title(self, title):
        return self.get_title(title)

    def do_click_on_finish_button(self):
        # self.driver.execute_script("window.scrollBy(0,1000)","")
        # btn = self.driver.find_element_by_xpath("//button[@id='cancel']")
        # self.driver.execute_script("arguements[0].scrollIntoView();",btn).
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.do_click(Locators.FINISH_BUTTON)