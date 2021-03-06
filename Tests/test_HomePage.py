import sys, os
from turtle import home

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Locators.Locators import Locators
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Locators.EnumsPackage.Enums import Sort_Productss

class Test_Home(BaseTest):
    
    @pytest.mark.order()
    def test_verify_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        title = homePage.get_title()
        assert title == TestData.HOME_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order()
    def test_verify_home_page_header(self): 
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        header = homePage.get_header_value()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)
        assert header == TestData.HOME_PAGE_HEADER

    @pytest.mark.order()
    def test_verify_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        notification = homePage.is_cart_icon_exist()
        assert notification
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

    @pytest.mark.order()
    def test_verify_product_sort_container(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.product_sort_container()
        for getValue in Sort_Productss:
            sortingNames  = self.driver.find_element_by_xpath(
                     "//*[@class='product_sort_container']//option[contains(text(),'%s')]" % str(getValue.value)) 
            assert sortingNames.text == getValue.value

    @pytest.mark.order()
    def test_verify_shopping(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_shopping()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order()
    def test_verify_sorting_Zto_A(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.product_sort_container()
        homePage.sort_product_High_to_Low()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)


    @pytest.mark.order()
    def test_verify_logout_into_app(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage.do_logout()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)