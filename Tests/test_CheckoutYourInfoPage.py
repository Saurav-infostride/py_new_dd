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
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage


class Test_CheckoutYourInfoPage(BaseTest):

    @pytest.mark.order(1)
    def test_verify_enter_info_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        addToCartPage = homePage
        time.sleep(5)
        homePage.do_shopping()
        time.sleep(5)
        homePage.do_click(Locators.CART_ICON)
        time.sleep(5)
        addToCartPage.do_click(Locators.CHECKOUT_BUTTON)
        time.sleep(5)
        checkoutyourInfoPage = addToCartPage
        checkoutyourInfoPage.do_enter_your_info()
        # addToCartPage = CheckoutYourInfoPage
        # CheckoutYourInfoPage.do_enter_your_info()