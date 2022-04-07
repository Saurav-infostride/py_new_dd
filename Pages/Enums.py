from enum import Enum

class Products(Enum):
    SAUCE_LABS_BACKPACK = "Sauce Labs Backpack"
    SAUCE_LABS_BIKE_LIGHT = 'Sauce Labs Bike Light'
    SAUCE_LABS_BOLTS_T_SHIRT = 'Sauce Labs Bolt T-Shirt'
    SAUCE_LABS_FLEECE_JACKET = 'Sauce Labs Fleece Jacket'
    SAUCE_LABS_ONESIE = 'Sauce Labs Onesie'
    TEST_ALL_THE_THINGS_T_SHIRT_RED = 'Test.allTheThings() T-Shirt (Red)'

        # SAUCE_LABS_BACKPACK = 1
    # SAUCE_LABS_BIKE_LIGHT = 2
    # SAUCE_LABS_BOLTS_T_SHIRT = 3
    # SAUCE_LABS_FLEECE_JACKET = 4
    # SAUCE_LABS_ONESIE = 5
    # TEST_ALL_THE_THINGS_T_SHIRT_RED = 6

class Sort_Products(Enum):
    NAME_Z_A = 2
    PRICE_LOW_TO_HIGH = 3
    PRICE_HIGH_TO_LOW = 4