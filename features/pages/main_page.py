from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    LOGO_GMAIL = By.XPATH, "//img[@class='gb_uc']"
    ROW_UNREAD_EMAIL = By.XPATH, "//div[@role='main']//tr[contains(@class, 'zE')]"
    ROW_ANY_EMAIL = By.XPATH, "//div[@role='main']//tr[contains(@class, 'zA')]"
    ROW_TODAYS_EMAIL = By.XPATH, "//div[@role='main']//tr[contains(@class, 'xW')]"
    ROW_SECURITY_EMAIL = By.XPATH, "//div[@role='main']//tr[contains(@class, 'zE')]//div[@class='yW']//span[@name='Google']/../../../.."
    BUTTON_INBOX = By.XPATH, '//a[@href="https://mail.google.com/mail/u/0/#inbox"]'

    CHECKBOX_SELECT_ALL = '//span[@role="checkbox"]'
    BUTTON_DELETE = '//div[@act="10"]'

    BUTTON_CHECK_ACTIVITY = By.XPATH, '//a[contains(@data-saferedirecturl, "https://www.google.com/url?q=https://accounts.google.com/AccountChooser")]'
    BUTTON_YES_IT_WAS_ME = By.XPATH, '//i[text()="done"]/..'
    LOGO_SECURITY_SUCCESSFULL = By.XPATH, '//img[contains(@src, "https://www.gstatic.com/identity/accountsettingssecuritycommon/success_light_mode")]'

    LINK = By.TAG_NAME, '//a'

    BUTTON_NOT_SPAM = By.XPATH, '//button[contains(@class, "bzq bzr")]'

    def _verify_page(self):
        self.on_this_page(self.LOGO_GMAIL)

    def confirm_security_email(self):
        self.click_on(self.BUTTON_CHECK_ACTIVITY)
        self.click_on(self.BUTTON_YES_IT_WAS_ME)
        self.get_element(self.LOGO_SECURITY_SUCCESSFULL)
        while len(self.driver.window_handles) > 1:
            self.driver.close()

    def click_all_links(self):
        all_links = self.get_elements(self.LINK)
        for link in all_links:
            try:
                self.click_on(link)
                sleep(3)
            except Exception:
                pass
            while len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
                self.driver.close()
                self.driver.switch_to.window(window_name=self.driver.window_handles[0])
