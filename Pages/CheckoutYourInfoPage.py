import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import xlrd
from Locators.Locators import Locators
from Pages.BasePage import BasePage

class CheckoutYourInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_enter_your_info(self):
        path = r"C://Users//SauravSharma//Pytest//Pytest_pom_dd//TestData.xlsx"
        workbook = xlrd.open_workbook(path)
        sheet=workbook.sheet_by_name("Sheet2")

        rowCount = sheet.nrows
        # cols = sheet.ncols
        # print(rowCount)
        # print(cols)
        for curr_row in range(1, rowCount):
            firstname = sheet.cell_value(curr_row, 0)
            lastname = sheet.cell_value(curr_row, 1)
            zipcode = sheet.cell_value(curr_row, 2)
            self.do_send_keys(Locators.FIRST_NAME, firstname)
            self.do_send_keys(Locators.LAST_NAME, lastname)
            self.do_send_keys(Locators.ZIP_POSTAL_CODE, zipcode)
            self.do_click(Locators.CONTINUE_BUTTON)
            # return HomePage(self.driver)