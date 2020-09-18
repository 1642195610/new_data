from selenium import webdriver
# 控制一系列的鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome(
    '../../../Documents/WeChat Files/ychzb1642195610ychzb/FileStorage/File/2020-04/chromedriver.exe')
# 打开QQ空间
driver.get('https://qzone.qq.com/')
# 先找到frame
first_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
# 切换到该frame中
driver.switch_to.frame(first_frame)
# 点击账号密码登陆
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# 输入账号密码
driver.find_element_by_xpath('//*[@id="u"]').send_keys('1104781249')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('Hai#1104781249')
# 点击登陆
driver.find_element_by_xpath('//*[@id="login_button"]').click()
# 等待一下,完全加载出滑块
sleep(2)
# 切换到滑块的iframe
huakuai_frame = driver.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
driver.switch_to.frame(huakuai_frame)
sleep(2)
# 找到滑块
huakuai = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')

# 初始距离
distance = 140
# perform(): 提交这个动作
while True:
    try:
        # 摁住滑块
        ActionChains(driver).click_and_hold(huakuai).perform()
        # 拖动滑块
        # move_by_offset(x,y): 水平方向  垂直方向
        ActionChains(driver).move_by_offset(distance, 0).perform()
        # 松手 释放移动
        ActionChains(driver).release().perform()
        # 让距离+1
        distance += 1
    except:
        print('页面跳转了')
        sleep(5)
        with open('QQ空间1.html','w',encoding='utf-8') as file:
            file.write(driver.page_source)
        break
sleep(5)
driver.quit()