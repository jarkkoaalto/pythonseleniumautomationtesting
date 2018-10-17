'''
Created on 17-10-2018
try find total numbers of links what is presented in ebay webpage
@author: Jarkko
'''

from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.ebay.com/")

totallinks = driver.find_elements_by_tag_name("a")
print("Total links : ",len(totallinks))
driver.close()