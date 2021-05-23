from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')

driver.find_element_by_xpath('//input[@type="email"]').send_keys('aliceerohina1990@gmail.com')
driver.find_element_by_xpath('//div[@id="identifierNext"]').click()
sleep(15)
driver.find_element_by_xpath('//input[@type="password"]').send_keys('depWec-0recvy-zurzex')
driver.find_element_by_xpath('//div[@id="passwordNext"]').click()

try:
    driver.find_element_by_xpath('//div[@id="submit_approve_access"]').click()
except Exception:
    pass

driver.find_element_by_xpath('//span[text()="Playground"]')
driver.get('https://gmail.com')

sleep(5)
unread_emails = driver.find_elements_by_xpath("//tr[contains(@class, 'zE')]")

for email in unread_emails:
    email.click()
    sleep(5)
    driver.get('https://mail.google.com/mail/u/0/#inbox')
    sleep(5)

driver.close()