import time
import pytest
from selenium.webdriver.common.by import By

from Framework.config.config import TestData
from Framework.utilities.BaseClass import BaseClass
from Framework.pageObjects.CheckoutPage import CheckOutPage


class HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.SHOP_URL)

    home = (By.LINK_TEXT, "Home")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    student = (By.CSS_SELECTOR, '#inlineRadio1')
    employee = (By.CSS_SELECTOR, '#inlineRadio2')
    entreprener = (By.CSS_SELECTOR, '#inlineRadio3')
    dob = (By.CSS_SELECTOR, "input[name='bday']")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")


    def get_home(self):
        self.do_click(self.home)

    def expects(self):
        angular = self.is_url_valid("angular")
        assert angular
        self.is_visible(self.submit)

    def get_name(self, name):
        self.do_send_keys(self.name, name)

    def get_email(self, email):
        self.do_send_keys(self.email, email)

    def get_password(self, password):
        self.do_send_keys(self.password, password)

    def get_checkbox(self):
        self.do_click(self.check)

    def get_gender(self, text):
        self.select_option_by_text(self.gender, text)

    def get_employment(self, value):
        log = self.getLogger()

        if value.lower() == "student":
            self.do_click(self.student)
        elif value.lower() == "employed":
            self.do_click(self.employee)
        else:
            log.info("INVALID EMPLOYMENT STATUS ERROR")
            pytest.fail("INVALID EMPLOYMENT STATUS ERROR", True)

    def get_dob(self, dob):
        self.do_send_keys(self.submit, dob)

    def get_submit(self):
        self.do_click(self.submit)
        self.is_visible(self.successMessage)
        text = self.get_text(self.successMessage)
        assert "Success" in text

    def get_shop(self):
        self.do_click(self.shop)
        checkout = CheckOutPage(self.driver)
        time.sleep(2)
        return checkout



