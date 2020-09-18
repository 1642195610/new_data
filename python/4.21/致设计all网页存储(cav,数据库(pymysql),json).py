#coding=utf-8
from selenium import webdriver
from lxml import etree
import csv
import time
import pymysql
import json
db = pymysql.connect("localhost","root","","百度贴吧改编码")
cursor = db.cursor()
t = 0
file = "致设计.csv"
header_csv = ["图片地址", "作品名字", "作品类型", "人气数", "点赞数", "评论数", "作者图片", "作者"]
with open(file, "w", encoding="utf-8-sig", newline="")as data:
    data_csv = csv.DictWriter(data, header_csv)
    data_csv.writeheader()
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.zhisheji.com/")
for page in range(1,4):
    print("第%s页开始"%(page))
    connect = driver.page_source
    connect = etree.HTML(connect)
    m = connect.xpath('//ul[@class="list"]/li')
    def shu(a):
        if len(a) > 0:
            a = a[0]
        else:
            a = "无"
        return a
    list = []
    for i in m:
        t += 1
        # 图片地址
        url = i.xpath('.//span/img/@src')
        url = shu(url)
        # 作品名字
        mz = i.xpath('.//span/img/@alt')
        mz = shu(mz)
        # 作品类型
        lx = i.xpath('./div[@class="desc"]/text()')
        lx = shu(lx)
        # 人气数,点赞数,评论数
        rqs, dzs, pls = i.xpath('.//em/text()')
        # 作者图片
        ta = i.xpath('.//a/img/@src')
        ta = shu(ta)
        # 作者
        zz = i.xpath('.//a/img/@alt')
        zz = shu(zz)
        dic = {
            "图片地址": url,
            "作品名字": mz,
            "作品类型": lx,
            "人气数": rqs,
            "点赞数": dzs,
            "评论数": pls,
            "作者图片": ta,
            "作者": zz
        }
        list.append(dic)
        with open("zsj.json", "w", encoding="utf-8")as filejson:
            json.dump({"data": list}, filejson, ensure_ascii=False, indent=4)
        with open(file, "a", encoding="utf-8-sig", newline="")as data:
            data_csv = csv.DictWriter(data, header_csv)
            data_csv.writerow(dic)
        sql = "insert into zsj (图片地址, 作品名字, 作品类型, 人气数, 点赞数, 评论数, 作者图片, 作者) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
        url, mz, lx, rqs, dzs, pls, ta, zz)
        cursor.execute(sql)
        print("插入%s条" % (t))
    if page == 1:
        driver.find_element_by_xpath('/html/body/div[9]/div[1]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="istj"]/div/div/a[@class="next"]').click()
    print("第%s页结束"%(page))
db.commit()
db.close()
time.sleep(3)
driver.quit()

