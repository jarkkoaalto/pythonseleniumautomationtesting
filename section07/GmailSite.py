from selenium import webdriver
driver=webdriver.Firefox()

driver.get("https://gmail.com")

#driver.find_element_by_xpath("//a[@identifierId]").click()
driver.find_element_by_name("Email").send_keys("BCD")
driver.find_element_by_css_selector("input[type='password']").send_keys("abc")
driver.find_element_by_id("signIn").click()
print(driver.find_element_by_id("signIn").text)
driver.find_element_by_xpath(".//*[@id='link-signup']").click()
print(driver.find_element_by_id("link-signin").is_displayed())
driver.find_element_by_xpath(".//*[@id='Passwd']").send_keys("1234556")
driver.find_element_by_xpath(".//*[@id='Passwd']").clear()
driver.find_element_by_xpath(".//*[@id='Passwd']").send_keys("12")
driver.find_element_by_link_text("Learn more").click()

