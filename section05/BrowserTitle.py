from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome('C:\\Python3.7\\chromedriver.exe')

browser = webdriver.Ie('C:\\Python3.7\\IEDriverServer.exe')

browser.get('https://google.com')
print(browser.title)

