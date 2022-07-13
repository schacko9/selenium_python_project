import pytest
import allure
from Framework.config.config import TestData
from Framework.utilities.BaseTest import BaseTest
from Framework.pageObjects.LoginPage import LoginPage


class TestLoginPage(BaseTest):

    @pytest.mark.regression
    def test_login_expects(self):
        self.login = LoginPage(self.driver)
        flag = self.login.expects()
        assert flag

    @pytest.mark.regression
    def test_login_expects2(self):
        self.login = LoginPage(self.driver)
        flag = self.login.expects()
        assert not flag                                                     #Intentional Failure

    @pytest.mark.regression
    def test_login_title(self):
        self.login = LoginPage(self.driver)
        title = self.login.get_login_page_title(TestData.TITLE)
        assert title == TestData.TITLE

    @pytest.mark.regression
    def test_login_signin(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_signin_link_visible()
        assert flag

    @pytest.mark.regression
    def test_login_terms(self):
        self.login = LoginPage(self.driver)
        text = self.login.is_terms_valid()
        assert "terms and conditions" in text

    @pytest.mark.regression
    def test_login_username_visibility(self):
        self.login = LoginPage(self.driver)
        text = self.login.is_username_visible()
        assert "Username" in text

    @pytest.mark.regression
    def test_login_password_visibility(self):
        self.login = LoginPage(self.driver)
        text = self.login.is_password_visible()
        assert "Password" in text

    @pytest.mark.regression
    def test_login_admin_visibility(self):
        self.login = LoginPage(self.driver)
        text = self.login.is_admin_visible()
        assert "Admin" in text

    @pytest.mark.regression
    def test_login_admin_clickable(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_admin_clickable()
        assert flag

    @pytest.mark.regression
    def test_login_user_visibility(self):
        self.login = LoginPage(self.driver)
        text = self.login.is_user_visible()
        assert "User" in text

    @pytest.mark.regression
    def test_login_user_clickable(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_user_clickable()
        assert flag

    @pytest.mark.regression
    def test_login_signin_clickable(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_signin_link_clickable()
        assert flag

    @pytest.mark.regression
    def test_login_blinking_text_visibility(self):
        self.login = LoginPage(self.driver)
        text = self.login.is_blinking_text_visible()
        assert "Free Access" in text

    @pytest.mark.regression
    def test_login_blinking_text_clickable(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_blinking_text_clickable()
        assert flag

    @pytest.mark.regression
    def test_login_blinking_text_link(self):
        self.login = LoginPage(self.driver)
        self.login.is_blinking_text_verify_link()

    @pytest.mark.regression
    def test_login_form_submission_positive(self):
        self.login = LoginPage(self.driver)
        self.login.get_credentials(TestData.USERNAME, TestData.PASSWORD)
        self.login.get_admin(role=False)
        self.login.get_employment(TestData.EMPLOYMENT)
        self.login.get_checkbox()
        self.product = self.login.get_signin()

    @pytest.mark.regression
    def test_login_form_submission_negative(self):
        self.login = LoginPage(self.driver)
        self.login.get_credentials(TestData.USERNAME2, TestData.PASSWORD2)
        self.login.get_admin(role=False)
        self.login.get_employment(TestData.EMPLOYMENT2)
        self.login.get_checkbox()
        self.product = self.login.get_signin_negative()




