from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get('https://yearbook.bits-hyderabad.ac.in/request')

elem=browser.find_element( "rc_select_4")

elem.send_keys("f20201778")
elem.send_keys(Keys.ARROW_DOWN)

elem2=browser.find_element("css_selector","ant-col ant-col-xs-24 ant-col-lg-4 css-szjdd9");
elem2.send_keys(Keys.ENTER)

print("done!")