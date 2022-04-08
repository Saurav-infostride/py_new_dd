from enum import Enum

class Products(Enum):
    SAUCE_LABS_BACKPACK = "Sauce Labs Backpack"
    SAUCE_LABS_BIKE_LIGHT = 'Sauce Labs Bike Light'
    SAUCE_LABS_BOLTS_T_SHIRT = 'Sauce Labs Bolt T-Shirt'
    SAUCE_LABS_FLEECE_JACKET = 'Sauce Labs Fleece Jacket'
    SAUCE_LABS_ONESIE = 'Sauce Labs Onesie'
    TEST_ALL_THE_THINGS_T_SHIRT_RED = 'Test.allTheThings() T-Shirt (Red)'

class Sort_Products(Enum):
    NAME_Z_A = 2
    PRICE_LOW_TO_HIGH = 3
    PRICE_HIGH_TO_LOW = 4

class Sort_Productss(Enum):
    NAME_Z_A = 'Name (Z to A)'
    PRICE_LOW_TO_HIGH = 'Price (low to high)'
    PRICE_HIGH_TO_LOW = 'Price (high to low)'

# class Sort_Products_Low_To_High(Enum):
#     SAUCE_LABS_BACKPACK = 
#     SAUCE_LABS_BIKE_LIGHT = 'Sauce Labs Bike Light'
#     SAUCE_LABS_BOLTS_T_SHIRT = 'Sauce Labs Bolt T-Shirt'
#     SAUCE_LABS_FLEECE_JACKET = 'Sauce Labs Fleece Jacket'
#     SAUCE_LABS_ONESIE = 'Sauce Labs Onesie'
#     TEST_ALL_THE_THINGS_T_SHIRT_RED = 'Test.allTheThings() T-Shirt (Red)'