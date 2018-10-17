from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.maximize_window()

driver.get("http://www.airindia.in/")

driver.find_element_by_partial_link_text("Book Flight").click()
#driver.implicitly_wait(4)

driver.find_element_by_xpath(".//*[@id='from']").send_keys("ban")
driver.implicitly_wait(4)
driver.find_element_by_partial_link_text("Thailand").click()
driver.find_element_by_css_selector("input[id='to']").send_keys("del")
driver.implicitly_wait(4)
driver.find_element_by_partial_link_text("Delhi").click()

dropdown = Select(driver.find_element_by_xpath(".//*[@id='_classType1']"))
dropdown.select_by_index(3)
dropdown.select_by_value("PremiumBusiness")

#dropdown.select_by_visible_text("Executive")

print(driver.find_element_by_xpath("//div[@id='divclasstype1']/span/span").text)

radio=driver.find_element_by_xpath("//input[@id='rdrules1']")
if radio.is_selected():
    print("True")
else: 
    print("False")