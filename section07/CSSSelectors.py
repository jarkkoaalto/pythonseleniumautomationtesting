from selenium import webdriver
driver=webdriver.Firefox()

driver.get("https://facebook.com")


driver.find_element_by_css_selector("input[data-testid='royal_login_button']").click()