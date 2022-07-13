import pytest
from selenium.webdriver.common.by import By
from Framework.pageObjects.ProductPage import ProductPage
from Framework.utilities.BaseClass import BaseClass
from Framework.config.config import TestData


class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    blinkText = (By.CSS_SELECTOR, ".blinkingText")
    doctext = (By.CSS_SELECTOR, ".inner-box")
    username = (By.CSS_SELECTOR, "input[name='username']")
    username_label = (By.CSS_SELECTOR, "label[for='username']")
    password = (By.CSS_SELECTOR, "input[type='password']")
    password_label = (By.CSS_SELECTOR, "label[for='password']")
    signIn = (By.CSS_SELECTOR, "#signInBtn")
    admin = (By.CSS_SELECTOR, "div.form-check-inline label:nth-child(1) span:nth-child(3)")
    admin_label = (By.CSS_SELECTOR, ".form-check-inline label:nth-child(1) span:nth-child(1)")
    user = (By.CSS_SELECTOR, "div.form-check-inline label:nth-child(2) span:nth-child(3)")
    user_label = (By.CSS_SELECTOR, ".form-check-inline label:nth-child(2) span:nth-child(1)")
    modal = (By.CSS_SELECTOR, ".modal-body")
    ok = (By.CSS_SELECTOR, ".btn-success")
    cancel = (By.CSS_SELECTOR, ".btn-secondary")
    dropdown = (By.CSS_SELECTOR, "select.form-control")
    checkbox = (By.CSS_SELECTOR, "#terms")
    terms = (By.CSS_SELECTOR, ".termsText")


    """Regression Actions"""
    def expects(self):
        login = self.is_url_valid("login")
        assert login
        return self.is_visible(self.blinkText)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signin_link_visible(self):
        return self.is_visible(self.signIn)

    def is_terms_valid(self):
        return self.get_text(self.terms)

    def is_username_visible(self):
        return self.get_text(self.username_label)

    def is_password_visible(self):
        return self.get_text(self.password_label)

    def is_admin_visible(self):
        return self.get_text(self.admin_label)

    def is_admin_clickable(self):
        return self.is_clickable(self.admin)

    def is_user_visible(self):
        return self.get_text(self.user_label)

    def is_user_clickable(self):
        return self.is_clickable(self.user)

    def is_signin_link_clickable(self):
        return self.is_clickable(self.signIn)

    def is_blinking_text_visible(self):
        return self.get_text(self.blinkText)

    def is_blinking_text_clickable(self):
        return self.is_clickable(self.blinkText)

    def is_blinking_text_verify_link(self):
        text = self.get_text(self.blinkText)
        assert "Free Access" in text
        flag = self.is_clickable(self.blinkText)
        assert flag

        self.do_click(self.blinkText)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

        text2 = self.get_text(self.doctext)
        assert "DOCUMENTS REQUEST" in text2
        login2 = self.is_url_valid("documents-request")
        assert login2
        title = self.get_title("Rahul Shetty Academy")
        assert title == "Rahul Shetty Academy"

    def get_signin_negative(self):
        log = self.getLogger()
        self.do_click(self.signIn)

        try:
            attribute = self.is_attribute_present(self.signIn, "value", "Sign In")
            assert attribute
            login2 = self.is_url_valid("login")
            assert login2
        except Exception as e:
            log.info("UNSUCCESSFUL LOGIN ATTEMPT ERROR")
            pytest.fail("UNSUCCESSFUL LOGIN ATTEMPT ERROR", True)
        else:
            log.info("Successful Login Attempt")

        product = ProductPage(self.driver)
        return product



    """Smoke Actions"""
    def get_credentials(self, user, password):
        self.do_send_keys(self.username, user)
        self.do_send_keys(self.password, password)
        log = self.getLogger()
        log.info(user)

    def get_admin(self, *, role: bool):
        if role:
            invis_modal = self.is_invisible(self.modal)
            assert invis_modal
            self.do_click(self.admin)
        else:
            self.do_click(self.user)
            vis_modal = self.is_visible(self.modal)
            assert vis_modal
            self.do_click(self.cancel)

            invis_modal = self.is_invisible(self.modal)
            assert invis_modal

            self.do_click(self.user)
            vis_modal = self.is_visible(self.modal)
            assert vis_modal
            self.do_click(self.ok)

    def get_employment(self, text):
        self.select_option_by_text(self.dropdown, text)

    def get_checkbox(self):
        terms = self.get_text(self.terms)
        assert "terms and conditions" in terms
        self.do_click(self.checkbox)

    def get_signin(self):
        log = self.getLogger()
        self.do_click(self.signIn)

        try:
            attribute = self.is_attribute_present(self.signIn, "value", "Sign In")
            assert attribute
            login2 = self.is_url_valid("login")
            assert login2
        except Exception as e:
            log.info("Successful Login Attempt")
        else:
            log.info("UNSUCCESSFUL LOGIN ATTEMPT ERROR")
            pytest.fail("UNSUCCESSFUL LOGIN ATTEMPT ERROR", True)

        product = ProductPage(self.driver)
        return product
