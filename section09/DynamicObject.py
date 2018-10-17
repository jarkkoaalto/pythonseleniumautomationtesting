'''
Created on 11.10.2018

@author: Jarkko
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://paytm.com")

driver.find_element_by_xpath("//input[contains(@id='mobile')]").send_keys("123233445")
driver.find_element_by_css_selector("[id*='amou']").send_keys("400")
# driver.find_element_by_xpath(".//input[@required='']").send_keys("123456789")