
import collections
import os,sys
from typing import Collection
from selenium.webdriver.support.ui import Select

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from pip import List
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Locators.EnumsPackage.Enums import Products, Sort_Products



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
        b = self.driver.find_element_by_xpath("(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.PRICE_LOW_TO_HIGH.value))
        b.click()
    
    def sort_product_High_to_Low(self):
        a = []
        all_spans = self.driver.find_elements_by_class_name("inventory_item_price")
        for span in all_spans:
            a.append(span.text.replace("$",""))
        assert a[0]<a[1], "products are not sorted"
            

        # beforeFilterPriceList = [self.driver.find_elements_by_class_name("inventory_item_price")]
        # # beforeFilterPriceList = abc ([])
        # # for i in beforeFilterPriceList:
        # #     beforeFilterPriceList.add(i.text().remove("$"))

        # abc = Select(self.driver.find_element(By.class_name("product_sort_container")))
        # abc.select_by_visible_text("Price (low to high")

        # afterFilterPriceList = [self.driver.find_elements_by_class_name("inventory_item_price")]
        # afterFilterPriceList = abc ([])
        # # for i in afterFilterPriceList:
        # #     afterFilterPriceList.add(i.text().remove("$"))

        # '''comparing'''
        # beforeFilterPriceList.sort()
        # assert(beforeFilterPriceList, afterFilterPriceList)
        
    ''' Add to Cart functionality'''
    def do_shopping(self):
        for i in Products:
            a = self.driver.find_element_by_xpath(
                "//div[contains(text(),'%s')]/following::button[1]" % str(i.value))
            a.click()
        self.do_click(Locators.CART_ICON)
            
    def do_logout(self):
        self.do_click(Locators.BURGER_MENU_BUTTON)
        self.do_click(Locators.LOGOUT_BUTTON)
