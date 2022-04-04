import sys, os

import webdrivermanager
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.by import By

class CheckoutYourInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''can be used to send the values'''
    # @pytest.mark.parametrize(  
    #     "firstname", "lastname", "postalcode",
    #     [
    #         ("saurav", "sharma", "hello")
    #     ]
    # )
    def do_enter_your_info(self):
        # '''Fetching the data from config file'''
        # self.do_send_keys(Locators.FIRST_NAME, TestData.FIRST_NAME)
        # time.sleep(5)
        # self.do_send_keys(Locators.LAST_NAME, TestData.LAST_NAME)
        # time.sleep(5)
        # self.do_send_keys(Locators.ZIP_POSTAL_CODE, TestData.POSTAL_CODE)
        # time.sleep(5)
        # self.do_click(Locators.CONTINUE_BUTTON)

            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//*[@class='input_error form_input'])[1]").send_keys("Saurav")
            time.sleep(10)
        
            # self.driver.find_element(By.XPATH, "(//div//input)[2]").click()
            self.driver.find_element(By.XPATH, "(//div//input)[2]").send_keys("Sharma")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "(//*[@class='input_error form_input'])[2]").send_keys("Sharma")
            self.driver.find_element(By.XPATH, "(//*[@class='input_error form_input'])[3]").send_keys(123445)
            self.driver.find_element(By.ID, "continue").click()


        # path = r"C://Users//SauravSharma//Pytest//Pytest_pom_dd_sauce_demo//TestData.xlsx"
        # workbook = xlrd.open_workbook(path)
        # sheet=workbook.sheet_by_name("Sheet2")

        # rowCount = sheet.nrows
        # # cols = sheet.ncols
        # # print(rowCount)
        # # print(cols)
        # for curr_row in range(1, rowCount):
        #     firstname = sheet.cell_value(curr_row, 0)
        #     lastname = sheet.cell_value(curr_row, 1)
        #     postalcode = sheet.cell_value(curr_row, 2)
        #     self.do_send_keys(Locators.FIRST_NAME, firstname)
        #     time.sleep(20)
        #     self.do_send_keys(Locators.LAST_NAME, lastname)
        #     time.sleep(20)
        #     self.do_send_keys(Locators.ZIP_POSTAL_CODE, postalcode)
        #     time.sleep(20)
        #     self.do_click(Locators.CONTINUE_BUTTON)
        