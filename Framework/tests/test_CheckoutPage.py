import pytest
import allure
from Framework.config.config import TestData
from Framework.utilities.BaseTest import BaseTest
from Framework.pageObjects.CheckoutPage import CheckOutPage


class TestCheckoutPage(BaseTest):

    @pytest.mark.regression
    def test_checkout_expects(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.expects()
        assert flag

    @pytest.mark.regression
    def test_checkout_button_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_checkout_visible()
        assert "Checkout" in text

    @pytest.mark.regression
    def test_checkout_button_clickable(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_checkout_clickable()
        assert flag

    @pytest.mark.regression
    def test_checkout_add_products(self):
        self.checkout = CheckOutPage(self.driver)
        self.checkout.get_add_products(TestData.LIST)
        length = len(TestData.LIST)
        count = self.checkout.get_checkout_count()
        assert length == count

    @pytest.mark.regression
    def test_checkout_continue_shopping_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_continue_shopping_visible()
        assert "Continue Shopping" in text

    @pytest.mark.regression
    def test_checkout_continue_shopping_clickable(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_continue_shopping_clickable()
        assert flag

    @pytest.mark.regression
    def test_checkout_continue_shopping_functionality(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_continue_shopping_functional()
        assert flag

    @pytest.mark.regression
    def test_checkout_checkout_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_cart_checkout_visible()
        assert "Checkout" in text

    @pytest.mark.regression
    def test_checkout_checkout_clickable(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_cart_checkout_clickable()
        assert flag

    @pytest.mark.regression
    def test_checkout_checkout_functionality(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_checkout_functional()
        assert flag

    @pytest.mark.regression
    def test_checkout_remove_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_cart_checkout_visible()
        assert "Checkout" in text

    @pytest.mark.regression
    def test_checkout_remove_clickable(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_cart_checkout_clickable()
        assert flag

    @pytest.mark.regression
    def test_checkout_remove_functionality(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_remove_functional()
        assert "0" in text

    @pytest.mark.regression
    def test_checkout_form_country_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_form_country_visible()
        assert "delivery location" in text

    @pytest.mark.regression
    def test_checkout_form_checkbox_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        text = self.checkout.is_form_checkbox_visible()
        assert "term & Conditions" in text

    @pytest.mark.regression
    def test_checkout_form_checkbox_clickable(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_form_checkbox_clickable()
        assert flag

    @pytest.mark.regression
    def test_checkout_form_checkbox_functionality(self):
        self.checkout = CheckOutPage(self.driver)
        self.checkout.is_form_checkbox_terms_functional()

    @pytest.mark.regression
    def test_checkout_form_purchase_visibility(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_form_purchase_visible()
        assert flag

    @pytest.mark.regression
    def test_checkout_form_purchase_clickable(self):
        self.checkout = CheckOutPage(self.driver)
        flag = self.checkout.is_form_purchase_clickable()
        assert flag

    @pytest.mark.regression
    def test_checkout_process(self):
        self.checkout = CheckOutPage(self.driver)
        self.checkout.expects()
        self.checkout.get_add_products(TestData.LIST)
        self.checkout.get_checkout()
        self.checkout.get_proceed()
        self.checkout.get_form(TestData.CODE, TestData.COUNTRY)
