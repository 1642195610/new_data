from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://email.163.com/')
iframe = driver.find_element_by_xpath('//div[@id="urs163Area"]/iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@name="email"]').send_keys("jzy18248316206")
driver.find_element_by_xpath('//*[@name="password"]').send_keys("7758258jiang@,.@")
driver.find_element_by_xpath('//*[@id="dologin"]').click()
sleep(2)
with open("163.html", "w", encoding="utf-8")as file:
    file =file.write(driver.page_source)
sleep(3)
driver.close()