import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_invisible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    def is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def is_attribute_present(self, by_locator, attribute, text):
        element = WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element_attribute(by_locator, attribute, text))
        return bool(element)

    def is_url_valid(self, text):
        url = WebDriverWait(self.driver, 15).until(EC.url_contains(text))
        return bool(url)

    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title

    def select_option_by_text(self, by_locator, text):
        by, locator = by_locator
        dropdown = Select(self.driver.find_element(by, locator))
        dropdown.select_by_visible_text(text)

