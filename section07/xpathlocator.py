from selenium import webdriver
driver=webdriver.Firefox()

driver.get("https://facebook.com")
driver.find_element_by_xpath("//input[@id='email']").send_keys("customised xpath")
driver.find_element_by_xpath(".//*[@id='u_0_q']").send_keys("xpath demo")
driver.find_element_by_xpath(".//*[@id='u_0_13']").click()
