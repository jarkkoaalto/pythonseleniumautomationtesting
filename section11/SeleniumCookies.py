'''
Created on 22.10.2018

@author: Jarkko
'''
from selenium import webdriver
from Framehandling import cromedriverpath
cromedriverpath = "C:\Python3.7\chromedriver.exe"
driver=webdriver.Chrome(cromedriverpath)
driver.get("https://google.fi")
co=driver.get_cookies()
print(len(co))
driver.delete_all_cookies()
col=driver.get_cookies()
print(len(col))
