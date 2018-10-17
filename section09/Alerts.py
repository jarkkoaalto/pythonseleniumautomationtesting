'''
Created on 11.10.2018

@author: Jarkko
'''
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.tizag.com/javascriptT/javascriptalert.php")
driver.find_element_by_xpath("//div[@class='display']/form/input").click()
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept() # Positive
# driver.switch_to_alert().dismiss() # Negative

# driver.switch_to_alert().send_keys("mitävain") if alert containd textfield and type somethink



