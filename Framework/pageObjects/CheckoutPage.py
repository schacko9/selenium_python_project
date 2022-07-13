import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Framework.config.config import TestData
from Framework.utilities.BaseClass import BaseClass


class CheckOutPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.SHOP_URL)

    title = (By.LINK_TEXT, "ProtoCommerce")
    body = (By.TAG_NAME, "body")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, ".btn-primary")
    remove = (By.CSS_SELECTOR, ".btn-danger")
    continue_shopping = (By.CSS_SELECTOR, ".btn-default")
    proceed = (By.CSS_SELECTOR, ".btn-success")
    total = (By.CSS_SELECTOR, "h3 strong")

    country = (By.ID, "country")
    country_label = (By.CSS_SELECTOR, "label[for='country']")
    suggestions = (By.CSS_SELECTOR, ".suggestions")
    suggestionsItems = (By.CSS_SELECTOR, ".suggestions ul")

    checkbox_label = (By.CSS_SELECTOR, "label[for='checkbox2']")
    checkbox_link = (By.CSS_SELECTOR, "label[for='checkbox2'] a")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    popup = (By.CSS_SELECTOR, "ngx-smart-modal[identifier='myModal'] div:nth-child(2)")
    popup_title = (By.CSS_SELECTOR, "ngx-smart-modal[identifier='myModal'] div:nth-child(2) h1")
    popup_text = (By.CSS_SELECTOR, "ngx-smart-modal[identifier='myModal'] div:nth-child(2) p")
    popup_close = (By.CSS_SELECTOR, "ngx-smart-modal[identifier='myModal'] div:nth-child(2) button.btn")
    popup_x = (By.CSS_SELECTOR, "ngx-smart-modal[identifier='myModal'] div:nth-child(2) button.nsm-dialog-btn-close")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    success = (By.CSS_SELECTOR, ".alert-success")

    """Regression Action"""
    def is_checkout_visible(self):
        return self.get_text(self.checkOut)

    def is_checkout_clickable(self):
        return self.is_clickable(self.checkOut)

    def get_checkout_count(self):
        checkout = self.get_text(self.checkOut)
        text = checkout.split("(")[1]
        count = text.split(")")[0]
        return int(count)

    def is_continue_shopping_visible(self):
        self.do_click(self.checkOut)
        return self.get_text(self.continue_shopping)

    def is_continue_shopping_clickable(self):
        self.do_click(self.checkOut)
        return self.is_clickable(self.continue_shopping)

    def is_continue_shopping_functional(self):
        self.do_click(self.checkOut)
        self.do_click(self.continue_shopping)
        return self.is_checkout_visible()

    def is_cart_checkout_visible(self):
        self.do_click(self.checkOut)
        return self.get_text(self.proceed)

    def is_cart_checkout_clickable(self):
        self.do_click(self.checkOut)
        return self.is_clickable(self.proceed)

    def is_checkout_functional(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        return self.is_clickable(self.submit)

    def is_cart_remove_visible(self):
        self.get_add_products(TestData.LIST2)
        self.do_click(self.checkOut)
        return self.get_text(self.remove)

    def is_cart_remove_clickable(self):
        self.get_add_products(TestData.LIST2)
        self.do_click(self.checkOut)
        return self.is_clickable(self.remove)

    def is_remove_functional(self):
        self.get_add_products(TestData.LIST2)
        self.do_click(self.checkOut)
        self.do_click(self.remove)
        return self.get_text(self.total)

    def is_form_country_visible(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        return self.get_text(self.country_label)

    def is_form_checkbox_visible(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        return self.get_text(self.checkbox_label)

    def is_form_checkbox_clickable(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        return self.is_clickable(self.checkbox)

    def is_form_checkbox_terms_functional(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        self.do_click(self.checkbox_link)

        flag = self.is_visible(self.popup)
        assert flag
        title = self.get_text(self.popup_title)
        assert "Terms And Conditions" in title
        text = self.get_text(self.popup_text)
        assert "legally binding" in text
        close = self.get_text(self.popup_close)
        assert "Close" in close
        close = self.is_clickable(self.popup_close)
        assert close
        x = self.is_clickable(self.popup_x)
        assert x

        self.do_click(self.popup_close)
        self.do_click(self.checkbox_link)
        flag2 = self.is_visible(self.popup)
        assert flag2
        self.do_click(self.popup_x)

    def is_form_purchase_visible(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        return self.is_attribute_present(self.submit, "value", "Purchase")

    def is_form_purchase_clickable(self):
        self.do_click(self.checkOut)
        self.do_click(self.proceed)
        return self.is_clickable(self.proceed)









    """Smoke Action"""
    def expects(self):
        shop = self.is_url_valid("shop")
        assert shop
        return self.is_visible(self.title)


    def get_add_products(self, productlist):
        log = self.getLogger()
        cards = self.driver.find_elements(*self.cardTitle)
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText in productlist:
                self.driver.find_elements(*self.cardFooter)[i].click()
                log.info("Added to cart: "+cardText)

    def get_checkout(self):
        self.do_send_keys(self.body, Keys.CONTROL + Keys.HOME)
        self.is_clickable(self.checkOut)
        self.do_click(self.checkOut)

    def get_proceed(self):
        self.is_clickable(self.remove)
        self.do_click(self.proceed)

    def get_form(self, code, country):
        self.do_send_keys(self.country, code)
        suggestions = self.is_visible(self.suggestions)
        assert suggestions

        items = self.driver.find_elements(*self.suggestionsItems)
        for item in items:
            if item.text == country:
                item.click()
                break
        self.do_click(self.checkbox)
        self.do_click(self.submit)

        success = self.is_visible(self.success)
        assert success
        text = self.get_text(self.success)
        assert "Success! Thank you!" in text
