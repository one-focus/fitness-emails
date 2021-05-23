from datetime import datetime
from time import sleep

from behave import *
from selenium.webdriver.common.by import By

from pages.main_page import MainPage

use_step_matcher('re')


@when('I remove from spam')
def remove_from_spam(context):
    main_page = MainPage(context.driver)


@when('I remove from (?P<directory>spam|inbox)')
def remove_from_spam(context, directory):
    main_page = MainPage(context.driver)
    if directory == 'spam':
        while main_page.is_element_displayed(main_page.ROW_ANY_EMAIL):
            main_page.click_on(main_page.ROW_ANY_EMAIL)
            main_page.click_on(main_page.BUTTON_NOT_SPAM)
    else:
        main_page.click_on(main_page.CHECKBOX_SELECT_ALL)
        main_page.click_on(main_page.BUTTON_DELETE)


@when('I read (?P<email_type>unread|all|security|today) emails')
def read_emails(context, email_type):
    main_page = MainPage(context.driver)
    if 'unread' in email_type:
        element = main_page.ROW_UNREAD_EMAIL
    elif 'security' in email_type:
        element = main_page.ROW_SECURITY_EMAIL
    else:
        element = main_page.ROW_ANY_EMAIL
    errors = []
    while main_page.is_element_displayed(element):
        try:
            main_page.click_on(element)
            if 'security' in email_type:
                main_page.confirm_security_email()
                main_page.click_on(main_page.BUTTON_INBOX)
            else:
                main_page.click_all_links()
        except Exception as e:
            errors.append(e)
    errors and RuntimeError('Errors found during email read:', errors)
