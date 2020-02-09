import selenium as sln
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string

import time



path="C:\\Users\\andre\\Desktop\\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://www.eduasistent.ro/")

usr = driver.find_element(by="name",value='log')
pws = driver.find_element(by="name", value='pwd') 
logbut= driver.find_element(by="name", value='wp-submit')
actions = sln.webdriver.ActionChains(driver)
actions.send_keys_to_element(usr,'youremail')
actions.send_keys_to_element(pws,'yourpass')
actions.click(logbut);
actions.perform()
#here you place your link from the course you whant screenshoted
driver.get("https://www.eduasistent.ro/wp-content/neuropatie/lectia2/story_html5.html?ID=3053163681673");
driver.implicitly_wait(15)
elms=driver.find_elements_by_xpath("//a[@class='cs-listitem list-item   ']")
actions = sln.webdriver.ActionChains(driver)
j=0

from time import sleep
for i in elms:
	actions = sln.webdriver.ActionChains(driver)
	actions.click(i)
	actions.perform()
	sleep(8)
	driver.save_screenshot("./neuropatie2/"+str(j)+i.get_attribute("innerText")+".png")
	j=j+1
