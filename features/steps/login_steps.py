from time import sleep

from behave import *
from behave import use_step_matcher
from selenium.common.exceptions import TimeoutException

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils import captcha

use_step_matcher('re')


@step('I open (?P<page_name>login|inbox|spam) page')
def open_page(context, page_name):
    base_url = context.config.get('settings', 'base_url')
    if page_name in ("inbox", "spam"):
        context.driver.get(f'{base_url}')
        MainPage(context.driver)
        url = f'{base_url}#{page_name}'
        context.driver.get(url)
        sleep(2)
    elif page_name == "login":
        context.driver.get(context.config.get('settings', 'playground_url'))
        LoginPage(context.driver)


@when('I log in')
def log_in(context):
    login_page = LoginPage(context.driver)
    login_page.type_in(login_page.FIELD_EMAIL, context.config.get('user', 'email'))
    login_page.click_on(login_page.BUTTON_CONFIRM_EMAIL)
    if login_page.get_elements(login_page.IMG_CAPTCHA):
        confirm_captcha(login_page)
        for i in range(5):
            if login_page.get_elements(login_page.ERROR_CAPTCHA):
                confirm_captcha(login_page)
            else:
                break
    login_page.type_in(login_page.FIELD_PASSWORD, context.config.get('user', 'password'))
    login_page.click_on(login_page.BUTTON_CONFIRM_PASSWORD)
    if login_page.get_elements(login_page.IMG_PROTECT_YOUR_ACCOUNT):
        login_page.click_on(login_page.BUTTON_CONFIRM_PROTECT_YOUR_ACCOUNT)
    try:
        login_page.get_element(login_page.LABEL_PLAYGROUND)
    except TimeoutException:
        if login_page.get_elements(login_page.BUTTON_NOT_NOW):
            login_page.click_on(login_page.BUTTON_NOT_NOW)
        if login_page.get_elements(login_page.BUTTON_SECURITY):
            login_page.click_on(login_page.BUTTON_SECURITY)
    finally:
        login_page.get_element(login_page.LABEL_PLAYGROUND)
    login_page.allow_not_secure_apps()


def confirm_captcha(login_page):
    filename = "Captcha.jpeg"
    captcha.download_photo(login_page.get_attribute(login_page.IMG_CAPTCHA, 'src'), filename)
    code = captcha.get_code(filename)
    login_page.type_in(login_page.FIELD_CAPTCHA, code)
    login_page.click_on(login_page.BUTTON_CONFIRM_EMAIL)


# use of data table example
@then('I see validation message for')
def check_message(context):
    for row in context.table:
        context.execute_steps(f'''
        When I type "{row['username']}" in username field
        When I type "{row['password']}" in password field
        When I click on login button
        Then I see "{row['text']}" on the page
        ''')
