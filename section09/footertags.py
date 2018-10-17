'''
Created on 17-10-2018
try find total numbers of footer links what is presented in ebay webpage
@author: Jarkko
'''
from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.ebay.com/")
footerlinks = driver.find_element_by_xpath(".//*[@id='footerFragment']")
footer = footerlinks.find_elements_by_tag_name("a")
print("Total footer links: ", len(footer))

driver.close()