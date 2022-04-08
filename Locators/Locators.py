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
    PRODUCT_SORT_CONTAINER = (By.XPATH, "//*[@class='product_sort_container']")
    # LOW_TO_HIGH = (By.XPATH, "//*[@class='product_sort_container']//following::option[@value='lohi']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    # NO_OF_ITEMS_IN_CART_DISPLAYED = (By.XPATH, "//span[text()='6']")
    HEADER = (By.XPATH, "//span[text()='Products']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')])[%s]")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    '''cart page'''
    CART_PAGE_HEADER = (By.XPATH, "//span[text()='Your Cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")

    '''CHECKOUT: YOUR INFORMATION'''
    CHECKOUT_YOUR_INFO_PAGE_HEADER = (By.XPATH, "//*[text()='Checkout: Your Information']")
    FIRST_NAME = (By.XPATH, "(//*[@class='input_error form_input'])[1]")
    LAST_NAME = (By.XPATH, "(//*[@class='input_error form_input'])[2]")
    ZIP_POSTAL_CODE = (By.XPATH, "(//*[@class='input_error form_input'])[3]")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='continue']")

    '''Checkout overview page'''
    CHECKOUT_OVERVIEW_PAGE_HEADER = (By.XPATH, "//*[text()='Checkout: Overview']")
    FINISH_BUTTON = (By.XPATH, "//button[text()='Finish']")
