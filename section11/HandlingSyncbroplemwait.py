'''
Created on 22.10.2018

@author: Jarkko
'''
from selenium import webdriver
chromedriverpath = "C:\Python3.7\chromedriver.exe"
driver=webdriver.Chrome(chromedriverpath)
 
driver.implicitly_wait(10)
driver.get("https://google.fi")

driver.save_screenshot("C:\home.png")


