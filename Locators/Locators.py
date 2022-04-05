from selenium.webdriver.common.by import By

class Locators:
    
    '''loginpage'''
    LOGIN_PAGE_TITLE = (By.XPATH, "//*[text()='Swag Labs']")
    EMAIL = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Epic sadface: Username and password do not match any user in this service']")

    '''homepage'''
    HOME_PAGE_TITLE = (By.XPATH, "//*[text()='Swag Labs']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    NO_OF_ITEMS_IN_CART_DISPLAYED = (By.XPATH, "//span[text()='1']")
    HEADER = (By.XPATH, "//span[@class='title']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')])[%s]")
    SAUCE_LABS_BACPACK = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    SAUCE_LABS_BIKE_LIGHT = (By.XPATH, "//*[@name='add-to-cart-sauce-labs-bike-light']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    '''cart page'''
    CART_PAGE_TITLE = (By.XPATH, "//span[text()='Your Cart']")
    ITEM = (By.XPATH, "//*[text()='Sauce Labs Backpack']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")

    '''CHECKOUT: YOUR INFORMATION'''
    CHECKOUT_YOUR_INFO_TITLE = (By.XPATH, "//*[text()='Checkout: Your Information']")
    FIRST_NAME = (By.XPATH, "(//*[@class='input_error form_input'])[1]")
    LAST_NAME = (By.XPATH, "(//*[@class='input_error form_input'])[2]")
    ZIP_POSTAL_CODE = (By.XPATH, "(//*[@class='input_error form_input'])[3]")
    CONTINUE_BUTTON = (By.ID, "continue")

    '''Checkout overview page'''
    CHECKOUT_OVERVIEW_TITLE = (By.XPATH, "Checkout: Overview")
    FINISH_BUTTON = (By.XPATH, "//button[text()='Finish']")
