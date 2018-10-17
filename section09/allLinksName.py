'''
Created on 17-10-2018
try to print all footerlinks names
@author: Jarkko
'''

from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()
myfile = open('footerlinks.txt', 'w')

driver.get("https://www.ebay.com/")

footerlinks = driver.find_element_by_xpath(".//*[@id='footerFragment']")
footer = footerlinks.find_elements_by_tag_name("a")
print("Total footer links: ", len(footer))
for obj in footer :
    link = obj.text
    myfile.write("%s\n" % link)
    print(obj.text)
    
myfile.close()
driver.close()





