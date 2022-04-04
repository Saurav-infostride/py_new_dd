import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Locators.Locators import Locators
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage

class Test_AddTOCartPage(BaseTest):
    
    @pytest.mark.order()
    def test_verify_cart_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        homePage.do_click(Locators.CART_ICON)
        cart_title = addToCartPage.get_element_text(Locators.CART_PAGE_TITLE)
        if cart_title == TestData.CART_PAGE_TITLE:
            allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)
        else:
            pass
            
    @pytest.mark.order()
    def test_verify_checkout_button(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        homePage.do_click(Locators.CART_ICON)
        addToCartPage.do_click(Locators.CHECKOUT_BUTTON)

    @pytest.mark.order()
    def test_verify_item_1_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        homePage.do_shopping()
        homePage.do_click(Locators.CART_ICON)
        assert addToCartPage.is_visible(Locators.ITEM_1)