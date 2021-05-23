from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import pages


@when('I click on {element_name}')
def step_impl(context, element_name):
    context.current_page.click_on(element_name)


@when('I type "{text}" in {field_name}')
def step_impl(context, text, field_name):
    context.current_page.type_in(field_name, text)


@then('I see "{text}" in {element}')
def step_impl(context, text, element):
    element_text = context.current_page.get_text(element)
    if text not in element_text:
        raise RuntimeError(f'{element} text is {element_text}. Expected: {text}')


@then('I see "{text}" on the page')
def step_impl(context, text):
    element = (By.TAG_NAME, 'body')
    WebDriverWait(context.driver, 5).until(
        ec.text_to_be_present_in_element(element, text), f'Unable to find text: {text}')


@step('I am on {page_name} page')
def init_screen(context, page_name):
    """Instantiating verifies that we're on that page"""
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@given('I open url: "{url}"')
def step_impl(context, url):
    context.driver.get(f'{context.config.get("settings", "base_url")}{url}')
