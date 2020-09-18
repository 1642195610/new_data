import requests
from bc.bc import sj_User_Agent,bccsv
import json
from lxml import etree
import csv
import time
import random
import pymysql
def wai():
    while True:
        try:
            url = "https://erds.58.com/zufang/"
            response = requests.get(url, headers=sj_User_Agent())
            print(response)
            print()
            response.encoding="utf-8"
            return response.text
            break
        except Exception as e:
            print("这个请求头不可用!!!%s" % (e))
def z(filename,mhtml,t):
    # with open(filename , "w" , encoding="utf-8")as filel:
    #     filel = filel.write(mhtml)
    erfile = etree.HTML(mhtml)
    # 标题
    bt = erfile.xpath('//div[@class="main-wrap"]/div[@class="house-title"]/h1/text()')[0]
    # 浏览量
    ll = erfile.xpath('//div[@class="main-wrap"]/div[@class="house-title"]/p/em/text()')[0]
    # 图片地址
    tp = erfile.xpath('//div[@class="main-wrap"]//div[@id="bigImg"]/img[@id="smainPic"]/@src')[0]
    # 付款方式
    fk = erfile.xpath('//div[@class="main-wrap"]//div[@class="house-pay-way f16"]//span[@class="instructions"]/text()')[0]
    # 租赁方式
    zl = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[1]/span[2]/text()')[0]
    # 房屋类型
    fw = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[2]/span[2]/text()')[0].replace(" ", "").replace("\n", "")
    # 朝向楼层
    cx = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[3]/span[2]/text()')[0].replace(" ", "").replace("\n", "")
    # 所在小区
    xq = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[4]/span[2]/a/text()')[0].replace(" ", "").replace("\n", "")
    # 所属区域
    qy = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[5]/span[2]/a/text()')[0].replace(" ", "").replace("\n", "")
    # 详细地址
    xx = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[6]/span[2]/text()')[0].replace(" ", "").replace("\n", "")
    # print(bt,ll,tp,fk,zl,fw,cx,xq,qy,xx)
    dic = {
        "标题": bt,
        "浏览量": ll,
        "图片地址": tp,
        "付款方式": fk,
        "租赁方式": zl,
        "房屋类型": fw,
        "朝向楼层": cx,
        "所在小区": xq,
        "所属区域": qy,
        "详细地址": xx
    }
    # print(dic)
    # return 0
    list.append(dic)
    # print(dic)
    bccsv(filename, dic)
    with open("租房.json", "w", encoding="utf-8")as file_json:
        file_json = json.dump({"total": t, "data": list}, file_json, ensure_ascii=False, indent=4)
    sql = "insert into zf (标题,浏览量,图片地址,付款方式,租赁方式,房屋类型,朝向楼层,所在小区,所属区域,详细地址) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (bt, ll, tp, fk, zl, fw, cx, xq, qy, xx)
    cursor.execute(sql)
    print("爬取%s条" % (t))

# with open("租房.html", "r", encoding="utf-8")as yifile:
#     yifile = yifile.read()


header_csv = ['标题', '浏览量', '图片地址', '付款方式', '租赁方式', '房屋类型', '朝向楼层', '所在小区', '所属区域', '详细地址']
filename = "租房.csv"
with open(filename, "w", encoding="utf-8-sig",newline="")as file_csv:
    file_csv = csv.DictWriter(file_csv,header_csv)
    file_csv.writeheader()
db = pymysql.connect("localhost","root","","yy")
cursor = db.cursor()
list = []
t = 0
for j in range(1,30):
    print("第%s页开始"%(j))
    yifile = etree.HTML(wai())
    yifile = yifile.xpath('//li[@class="house-cell"]/div[@class="img-list"]/a/@href')
    print(yifile,len(yifile))
    for i in yifile:
        # print(i)
        while True:
            sj = random.randint(1,5)
            time.sleep(sj)
            try:
                murl = i
                erresponse = requests.get(murl, headers=sj_User_Agent())
                erresponse.encoding = "utf-8"
                print(erresponse)
                erresponse = erresponse.text
                # with open("3.html", "w", encoding="utf-8")as filel:
                # filel = filel.write(erresponse)
                break
            except Exception as e:
                print("这个<二级>请求头不可用!!!%s"%(e))
        # with open("3.html" , "w" , encoding="utf-8")as filel:
        #     filel = filel.write(erresponse)
        t += 1
        # try:
        z(filename, erresponse, t)
        # except Exception as e:
        #     print("访问频繁%s"%(e))
        # with open("4.html", "w", encoding="utf-8")as erfile:
        #     erfile = erfile.write(erresponse.text)
    print("第%s页结束"%(j))
db.commit()
db.close()



