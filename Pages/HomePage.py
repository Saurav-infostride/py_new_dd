
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import xlrd
from Pages.AddToCartPage import AddToCartPage
from Pages.BasePage import BasePage
from Locators.Locators import Locators

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

    def is_cart_icon_clickable(self):
        self.do_click(Locators.CART_ICON)
        return AddToCartPage(self.driver)

    def get_header_value(self):
        return self.get_element_text(Locators.HEADER)

    ''' Add to Cart functionality'''
    def do_shopping(self):
        self.do_click(Locators.SAUCE_LABS_BACPACK)
        self.do_click(Locators.SAUCE_LABS_BIKE_LIGHT)

    def do_logout(self):
        self.do_click(Locators.BURGER_MENU_BUTTON)
        self.do_click(Locators.LOGOUT_BUTTON)

    # def do_enter_your_info(self):
    #     path = r"C://Users//SauravSharma//Pytest//Pytest_pom_dd//TestData.xlsx"
    #     workbook = xlrd.open_workbook(path)
    #     sheet=workbook.sheet_by_name("Sheet2")

    #     rowCount = sheet.nrows
    #     for curr_row in range(1, rowCount):
    #         firstname = sheet.cell_value(curr_row, 0)
    #         lastname = sheet.cell_value(curr_row, 1)
    #         zipcode = sheet.cell_value(curr_row, 2)
    #         self.do_send_keys(Locators.FIRST_NAME, firstname)
    #         self.do_send_keys(Locators.LAST_NAME, lastname)
    #         self.do_send_keys(Locators.LAST_NAME, zipcode)
    #         self.do_click(Locators.CONTINUE_BUTTON)