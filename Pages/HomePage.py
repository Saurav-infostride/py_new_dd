import os,sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Pages.Enums import Products, Sort_Products



class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

    def get_header_value(self):
        return self.get_element_text(Locators.HEADER)

    def product_sort_container(self):
        for i in Sort_Products:
            b = self.driver.find_element_by_xpath(
                "(//*[@class='product_sort_container']//option)[%s]" % str(i.value))
            b.click()

    ''' Add to Cart functionality'''
    def do_shopping(self):
        for i in Products:
            a = self.driver.find_element_by_xpath(
                "//div[contains(text(),'%s')]/following::button[1]" % str(i.value))
            a.click()
            
    def click_on_cart_icon(self):
        self.do_click(Locators.CART_ICON)      

    def do_logout(self):
        self.do_click(Locators.BURGER_MENU_BUTTON)
        self.do_click(Locators.LOGOUT_BUTTON)
