import requests
from save.save import h
from lxml import etree
import csv
import pymysql
#连接数据库("主机名","用户名","密码","数据库名")
db = pymysql.connect("localhost","root","","百度贴吧改编码")
#创建游标对象
cursor = db.cursor()
url = "https://tieba.baidu.com/f?ie=utf-8&kw=%E9%A3%8E%E6%99%AF&fr=search"
response = requests.get(url , headers = h())
response = response.text
response = response.replace("<!--","").replace("-->","")
response = etree.HTML(response)
response = response.xpath('//div//div[@class="col2_right j_threadlist_li_right "]')
def cd(a):
    if len(a) >0 :
        a = a[0]
    else:
        a = "无"
    return a
header = ["标题","主题作者","内容","内容图片地址","时间"]
with open("百度贴吧.csv","w",encoding="utf-8-sig",newline="")as file:
    file = csv.DictWriter(file,header)
    file.writeheader()
    t = 0
for m in response:
    t += 1
    #标题
    bt = m.xpath('./div//a/@title')
    bt = cd(bt)
    #主题作者
    zz = m.xpath('.//div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author "]/@title')
    zz = cd(zz)
    #内容
    nr = m.xpath('.//div[@class="threadlist_text pull_left"]/div/text()')
    nr = cd(nr)
    nr = str(nr).replace("\n","").replace(" ","")
    #内容图片地址
    nrtp = m.xpath('.//div[@class="small_wrap j_small_wrap"]//div[@class="small_list_gallery"]/ul/li/a/img/@bpic')
    if len(nrtp) == "":
        nrtp = "无"
    else:
        nrtp = ",".join(nrtp)
    #时间
    sj = m.xpath('./div[@class="threadlist_detail clearfix"]/div[@class="threadlist_author pull_right"]/span[@title="最后回复时间"]/text()')
    sj = cd(sj)
    sj = sj.replace("\r\n","").replace(" ","")
    dict = {
        "标题": bt,
        "主题作者" : zz,
        "内容" : nr,
        "内容图片地址" : nrtp,
        "时间" : sj
    }
    with open("百度贴吧.csv","a",encoding="utf-8-sig",newline="")as file:
        file = csv.DictWriter(file,header)
        file.writerow(dict)
    #建立sql语句
    sql = "insert into baidutiebagaibianma (标题, 主题作者, 内容, 内容图片地址, 时间) values ('%s', '%s', '%s', '%s', '%s')"%(bt, zz, nr, nrtp, sj)
    #执行sql语句
    cursor.execute(sql)
    print("插入%s"%(t))
#提交
db.commit()
# 关闭数据库
db.close()
