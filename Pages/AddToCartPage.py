import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage

class AddToCartPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def get_add_to_cart_page_title(self, title):
            return self.get_title(title)

        def is_item_1_exist_in_cart(self):
            return self.is_visible(Locators.ITEM_1)

        def do_click_checkout_button(self):
            self.do_click(Locators.CHECKOUT_BUTTON)
            return CheckoutYourInfoPage(self.driver)

