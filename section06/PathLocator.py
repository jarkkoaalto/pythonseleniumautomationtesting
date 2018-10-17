from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://facebook.com")

driver.find_element_by_xpath(".//*[@id='u_0_3']").click()
driver.find_element_by_xpath(".//*[@id='email']").send_keys("xpath demo")