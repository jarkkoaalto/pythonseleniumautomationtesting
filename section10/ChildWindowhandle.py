'''
Created on 18.10.2018

@author: Jarkko
'''
from selenium import webdriver
driver=webdriver.Firefox()

driver.get("https://accounts.google.com/signin/v2/identifier?service=accountsettings&passive=1209600&osid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fintro&followup=https%3A%2F%2Fmyaccount.google.com%2Fintro&csig=AF-SEnb5_fDz1F3kgqyZ%3A1539872180&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/content/div/div/a").click()
print("before switching")
parent = driver.current_window_handle
print(driver.title)

driver.switch_to_window(driver.window_handles[-1])  # that return child window
child = driver.current_window_handle
print("After switching")
print(driver.title)


driver.switch_to_window(parent)
print("Switching back")
print(driver.title)
