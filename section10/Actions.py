'''
Created on 20.10.2018

@author: Jarkko
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()


driver.get("http://www.spicejet.com")
driver.maximize_window()

driver.get("https://www.spicejet.com/InvestorsFinancialInformation.aspx")

driver.implicitly_wait(4)
driver.get("http://corporate.spicejet.com/Content/pdf/2016-17AnnualReport.pdf")

