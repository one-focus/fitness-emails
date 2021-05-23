from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class LoginPage(BasePage):
    FIELD_EMAIL = By.XPATH, '//input[@type="email"]'
    FIELD_PASSWORD = By.XPATH, '//input[@type="password"]'
    FIELD_CAPTCHA = By.ID, 'ca'
    ERROR_CAPTCHA = By.XPATH, '//div[@aria-live="assertive"]'

    BUTTON_CONFIRM_EMAIL = By.XPATH, '//div[@id="identifierNext"]//button'
    BUTTON_CONFIRM_PASSWORD = By.ID, 'passwordNext'
    IMG_CAPTCHA = By.ID, 'captchaimg'

    BUTTON_SECURITY = By.ID, 'submit_approve_access'

    BUTTON_NOT_NOW = By.XPATH, '(//div[@aria-live="polite"]/..//div[@role="button"])[1]'

    IMG_PROTECT_YOUR_ACCOUNT = By.XPATH, '//img[@src="https://www.gstatic.com/identity/boq/accounthealthinterstitialsui/images/dont_get_locked_out.png"]'
    BUTTON_CONFIRM_PROTECT_YOUR_ACCOUNT = '(//div[@role="button"])[2]'

    LABEL_PLAYGROUND = By.XPATH, '//span[text()="Playground"]'

    SWITCH_LESS_SECURE = By.XPATH, '//input[@aria-checked="false"]'

    def _verify_page(self):
        self.on_this_page(self.FIELD_EMAIL)

    def allow_not_secure_apps(self):
        self.driver.get("https://myaccount.google.com/lesssecureapps")
        if self.get_elements(self.SWITCH_LESS_SECURE):
            self.click_on(self.SWITCH_LESS_SECURE)