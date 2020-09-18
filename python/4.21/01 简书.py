from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.jianshu.com/")
connect = driver.page_source
def s(a):
    if a == 1:
        with open("简书.html", "w", encoding="utf-8")as file:
            file = file.write(connect)
    else :
        with open("简书.html", "a", encoding="utf-8")as file:
            file = file.write(connect)
for page in range(1,4):
    print("第%s页开始"%(page))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    print("第%s页结束"%(page))
for page in range(1,5):
    print("点击第%s个按钮开始"% (page))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a').click()
    sleep(2)
    print("点击第%s个按钮结束"% (page))
    s(page)
sleep(3)
driver.quit()