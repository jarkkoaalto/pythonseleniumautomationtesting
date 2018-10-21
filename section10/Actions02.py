'''
Created on 21.10.2018

@author: Jarkko
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()


driver.get("https://www.google.com")
driver.maximize_window()
ActionChains(driver)
search = driver.find_element_by_class_name("gsfi")
# RightClicking
ActionChains(driver).move_to_element(search).context_click(search).perform()