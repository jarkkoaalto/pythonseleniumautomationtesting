from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://facebook.com")

#print(driver.current_url)



# Name Attribute
driver.find_element_by_name("firstname").send_keys("First")
driver.find_element_by_id("u_0_n").send_keys("Last")

driver.find_element_by_id("u_0_q").send_keys("first.last@df.com")
driver.find_element_by_id("u_0_t").send_keys("first.last@df.com")
driver.find_element_by_id("u_0_x").send_keys("!1234567890!")

#driver.close()