import sys, os
import time
from pytest import yield_fixture

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import xlrd
from Locators.Locators import Locators
from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions for login page'''
    '''this method is use to get the page title'''
    def get_login_page_title(self, title):
        return self.get_title(title)

    '''this is use to login to application'''
    def do_login(self):
        path = r"C://Users//SauravSharma//Pytest//Pytest_pom_dd_sauce_demo//TestData.xlsx"
        workbook = xlrd.open_workbook(path)
        sheet=workbook.sheet_by_name("login")

        rowCount = sheet.nrows
        for curr_row in range(1, rowCount):
            username = sheet.cell_value(curr_row, 0)
            password = sheet.cell_value(curr_row, 1)
            self.do_send_keys(Locators.EMAIL, username)
            self.do_send_keys(Locators.PASSWORD, password)
            self.do_click(Locators.LOGIN_BUTTON)
            return HomePage(self.driver)
    
    '''this is use to login to application with incorrect credentials'''
    def do_login_with_incorrect_credentials(self):
        path = r"C://Users//SauravSharma//Pytest//Pytest_pom_dd_sauce_demo//TestData.xlsx"
        workbook = xlrd.open_workbook(path)
        sheet=workbook.sheet_by_name("login")

        rowCount = sheet.nrows
        for curr_row in range(2, rowCount):
            username = sheet.cell_value(curr_row, 1)
            password = sheet.cell_value(curr_row, 2)
            self.do_send_keys(Locators.EMAIL, username)
            self.do_send_keys(Locators.PASSWORD, password)
            self.do_click(Locators.LOGIN_BUTTON)
