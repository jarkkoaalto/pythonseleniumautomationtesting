'''
Created on 21.10.2018

@author: Jarkko
'''
from selenium import webdriver
cromedriverpath="C:\Python3.7\chromedriver.exe"
driver=webdriver.Chrome(cromedriverpath)


driver.get("https://jqueryui.com/tooltip/")
fra = driver.find_element_by_class_name("demo-frame")
driver.switch_to_frame(fra)
driver.find_element_by_xpath(".//*[@id='age']").send_keys("435677")

driver.switch_to_default_content()
driver.find_element_by_xpath("//*[@id='sidebar']/aside[1]/ul/li[1]/a").click()