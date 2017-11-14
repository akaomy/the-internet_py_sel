from selenium import webdriver
from expects import *


driver = webdriver.Chrome("drivers/chromedriver")

@given(u'I navigate to the basic auth page')
def navigate_to_basic_auth_page(context):
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

@given(u'I should see {actual_basic_auth_success_message} the success message')
def verify_basic_auth_success_message(context, actual_basic_auth_success_message):
    actual_basic_auth_success_message = driver.find_element_by_xpath("//div[@class='example']/p").text
    expected_basic_auth_success_message = "Congratulations! You must have the proper credentials."
    expect(actual_basic_auth_success_message).to(contain(expected_basic_auth_success_message))

	# try:
	# 	expect(actual_basic_auth_success_message).to(contain(expected_basic_auth_success_message)).until(True)
	# finally:
	# 	driver.quit()

@then(u'I close the browser')
def close_browser(context):
    driver.quit()