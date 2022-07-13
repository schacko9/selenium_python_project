import time
from selenium.webdriver.common.by import By

from Framework.config.config import TestData
from Framework.utilities.BaseClass import BaseClass
from Framework.pageObjects.HomePage import HomePage


class ProductPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.SHOP_URL)


    title = (By.LINK_TEXT, "ProtoCommerce")
    home = (By.LINK_TEXT, "Home")
    shop = (By.LINK_TEXT, "Shop")
    category = (By.LINK_TEXT, "Category 1")
    checkout = (By.CSS_SELECTOR, ".btn-primary")

    def expects(self):
        shop = self.is_url_valid("shop")
        assert shop
        self.is_visible(self.title)

    def get_home(self):
        self.do_click(self.home)

    def get_shop(self):
        self.do_click(self.shop)

    def get_category(self):
        self.do_click(self.category)

    def getCheckout(self):
        self.do_click(self.checkout)
        home = HomePage(self.driver)
        time.sleep(2)
        return home
