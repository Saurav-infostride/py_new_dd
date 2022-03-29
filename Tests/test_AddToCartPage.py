import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Locators.Locators import Locators
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.AddToCartPage import AddToCartPage


class Test_AddTOCartPage(BaseTest):
    
    @pytest.mark.order(2)
    def test_verify_cart_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        homePage.do_click(Locators.CART_ICON)
        cart_title = addToCartPage.get_element_text(Locators.CART_PAGE_TITLE)
        time.sleep(5)
        assert cart_title == TestData.CART_PAGE_TITLE
        time.sleep(5)
        # addToCartPage = homePage.do_click()
        # cart_title = addToCartPage.get_element_text(Locators.CART_PAGE_TITLE)
        # assert cart_title == TestData.CART_PAGE_TITLE
        # allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)

    @pytest.mark.order(17)
    def test_verify_checkout_button(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        homePage.do_click(Locators.CART_ICON)
        addToCartPage.do_click(Locators.CHECKOUT_BUTTON)
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order(3)
    def test_verify_item_1_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        time.sleep(5)
        homePage.do_shopping()
        time.sleep(5)
        homePage.do_click(Locators.CART_ICON)
        time.sleep(5)
        assert addToCartPage.is_visible(Locators.ITEM_1)
        time.sleep(5)

    @pytest.mark.order(4)
    def test_verify_item_2_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        time.sleep(5)
        homePage.do_shopping()
        time.sleep(5)
        homePage.do_click(Locators.CART_ICON)
        time.sleep(5)
        assert addToCartPage.is_visible(Locators.ITEM_2)