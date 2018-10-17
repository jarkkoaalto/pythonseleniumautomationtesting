from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Hi Selenium")
# Open Firefox Browser an navicate to google home page
driver = webdriver.Firefox()
# Hit the URL
driver.get("https://www.google.section04")
#
print(driver.current_url)
print(driver.title)


print("Navigatinng to Gmail")
driver.get("https://gmail.section04")
print(driver.title)

print("Come back google home page")
driver.back()
print(driver.title)

driver.forward()
print("Come back to gmail home page")
print(driver.title)

print("Frefresh page")
driver.refresh()
print(driver.title)

driver.maximize_window()

driver.close()
driver.quit()