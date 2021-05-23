import abc
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        pass

    def on_this_page(self, *args):
        for locator in args:
            self.get_element(locator)

    def click_on(self, locator):
        self.get_clickable_element(locator).click()

    def is_element_displayed(self, locator):
        try:
            self.get_element(locator, timeout=2)
        except TimeoutException:
            return False
        return True



    def type_in(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.get_element(locator).get_attribute(attribute)

    def get_element(self, locator, timeout=15):
        expected_condition = ec.visibility_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Unable to locate element: "{locator}"')

    def get_elements(self, locator, timeout=2):
        expected_condition = ec.visibility_of_element_located(locator)
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_condition, message=f'Unable to locate elements: "{locator}"')
        except TimeoutException:
            return []

    def get_clickable_element(self, locator, timeout=15):
        sleep(2)
        expected_condition = ec.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Unable to locate element: {locator}')

    def get_clickable_elements(self, locator, timeout=15):
        sleep(2)
        expected_condition = ec.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Unable to locate element: {locator}')
