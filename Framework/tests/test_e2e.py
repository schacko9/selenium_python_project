import pytest
import allure
from Framework.config.config import TestData
from Framework.utilities.BaseTest import BaseTest
from Framework.pageObjects.LoginPage import LoginPage


class TestE2E(BaseTest):

    @pytest.mark.smoke
    def test_e2e(self):
        self.login = LoginPage(self.driver)
        self.login.expects()
        self.login.get_credentials(TestData.USERNAME, TestData.PASSWORD)
        self.login.get_admin(role=False)
        self.login.get_employment(TestData.EMPLOYMENT)
        self.login.get_checkbox()
        self.product = self.login.get_signin()

        self.product.expects()
        self.product.get_home()
        self.product.get_shop()
        self.product.get_category()
        self.product.get_shop()
        self.home = self.product.getCheckout()

        self.home.get_home()
        self.home.expects()
        self.home.get_name("Slomo Chacko")
        self.home.get_email("slomochacko0@gmail.com")
        self.home.get_password("chacko1")
        self.home.get_checkbox()
        self.home.get_gender("Female")
        self.home.get_employment("Student")
        self.home.get_dob("06-10-1998")
        self.home.get_submit()
        self.checkout = self.home.get_shop()

        self.checkout.expects()
        self.checkout.get_add_products(TestData.LIST)
        self.checkout.get_checkout()
        self.checkout.get_proceed()
        self.checkout.get_form(TestData.CODE, TestData.COUNTRY)