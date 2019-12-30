
#automactically facebook log

from selenium import webdriver

a=webdriver.Firefox()

a.get("https://www.facebook.com/")
a.find_element_by_xpath("//input[@id='email']").send_keys("enter email id")
a.find_element_by_xpath("//input[@id='pass']").send_keys("enter password")
a.find_element_by_xpath("//label[@id='loginbutton']").click()
a.quit()
