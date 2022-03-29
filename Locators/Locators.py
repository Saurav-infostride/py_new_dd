from telnetlib import LOGOUT
from selenium.webdriver.common.by import By

class Locators:
    
    EMAIL = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Epic sadface: Username and password do not match any user in this service']")

    '''homepage'''
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    NO_OF_ITEMS_IN_CART_DISPLAYED = (By.XPATH, "//span[text()='2']")
    HEADER = (By.XPATH, "//span[@class='title']")
    SAUCE_LABS_BACPACK = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    SAUCE_LABS_BIKE_LIGHT = (By.XPATH, "//*[@name='add-to-cart-sauce-labs-bike-light']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    '''cart page'''
    CART_PAGE_TITLE = (By.XPATH, "//span[text()='Your Cart']")
    ITEM_1 = (By.XPATH, "//*[text()='Sauce Labs Backpack']")
    ITEM_2 = (By.XPATH, "//*[text()='Sauce Labs Bike Light']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")

    '''CHECKOUT: YOUR INFORMATION'''
    CHECKOUT_YOUR_INFO = (By.XPATH, "//span[text()='Checkout: Your Information']")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    '''checkout complete page'''
    CHECKOUT_COMPLETE_PAGE = (By.XPATH, "//*[text()='Checkout: Complete!']")
    THANK_YOU_FOR_ORDER = (By.XPATH, "//*[text()='THANK YOU FOR YOUR ORDER']")
    BACK_TO_HOME_PAGE = (By.XPATH, "//button[text()='Back Home']")
