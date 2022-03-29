import sys, os

from Locators.Locators import Locators
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.AddToCartPage import AddToCartPage

class Test_Home(BaseTest):
    
    @pytest.mark.order(4)
    def test_verify_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        title = homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)

    @pytest.mark.order(5)
    def test_verify_home_page_header(self): 
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        header = homePage.get_header_value()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)
        assert header == TestData.HOME_PAGE_HEADER

    @pytest.mark.order(6)
    def test_verify_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        notification = homePage.is_cart_icon_exist()
        assert notification
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

    ''' Add to Cart functionality'''
    @pytest.mark.order(7)
    def test_verify_shopping(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_shopping()
        items_in_cart = homePage.get_element_text(Locators.NO_OF_ITEMS_IN_CART_DISPLAYED)
        assert items_in_cart == TestData.ITEMS_IN_CART
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)

    @pytest.mark.order(8)
    def test_verify_logout_into_app(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_logout()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)