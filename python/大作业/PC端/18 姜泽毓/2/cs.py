#coding=utf-8
import requests
from bc.bc import sj_User_Agent,bccsv
from lxml import etree
import csv
import pymysql
import json
list = []
def cs(a,j):
    t = 0
    # with open("音乐二级.html", "r", encoding="utf-8")as erfile:
    #     erfile = erfile.read()
    erfile = etree.HTML(a)
    r = erfile.xpath('//div//div//div[@class="main-body"]/div[@class="songlist-list"]/ul/li')
    filename = "音乐.csv"
    header_csv = ['最热图片地址', '最热热度', '最热歌曲名', '最热来自', '最热类型', '最新图片地址', '最新热度', '最新歌曲名', '最新来自', '最新类型']
    with open(filename, "w", encoding="utf-8-sig", newline="")as csv_file:
        csv_file = csv.DictWriter(csv_file, header_csv)
        csv_file.writeheader()
    db = pymysql.connect("localhost", "root", "", "yy")
    cursor = db.cursor()
    for m in r:
        t += 1
        # 最热
        # 最热图片地址
        murl = m.xpath('./div/img/@src')[0]
        # 最热热度
        rd = m.xpath('./div/div[@class="num"]/span/text()')[0].replace("\n", "").replace(" ", "").replace("\r","")
        # 最热歌曲名
        gqm = m.xpath('./p[@class="text-title"]/a/text()')[0]
        # 最热来自
        lz = m.xpath('./p[@class="text-user"]/text()')[0]
        # 最热类型
        lx = m.xpath('./p[@class="text-user"]/span/text()')[0]
        # 最新
        # 最新图片地址
        murl2 = m.xpath('./div/img/@src')[0]
        # 最新热度
        rd2 = m.xpath('./div/div[@class="num"]/span/text()')[0].replace("\n", "").replace(" ", "").replace("\r","")
        # 最新歌曲名
        gqm2 = m.xpath('./p[@class="text-title"]/a/text()')[0]
        # 最新来自
        lz2 = m.xpath('./p[@class="text-user"]/text()')[0]
        # 最新类型
        lx2 = m.xpath('./p[@class="text-user"]/span/text()')[0]
        # print(murl,rd,gqm,lz,lx,murl2,rd2,gqm2,lz2,lx2)
        dic = {
            "最热图片地址": murl,
            "最热热度": rd,
            "最热歌曲名": gqm,
            "最热来自": lz,
            "最热类型": lx,
            "最新图片地址": murl2,
            "最新热度": rd2,
            "最新歌曲名": gqm2,
            "最新来自": lz2,
            "最新类型": lx2
        }
        list.append(dic)
        bccsv(filename, dic)
        sql = "insert into yy (最热图片地址,最热热度,最热歌曲名,最热来自,最热类型,最新图片地址,最新热度,最新歌曲名,最新来自,最新类型) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(murl,rd,gqm,lz,lx,murl2,rd2,gqm2,lz2,lx2)
        cursor.execute(sql)
        with open("音乐.json", "w", encoding="utf-8")as j_file:
            j_file = json.dump({"total": t * j, "data": list}, j_file, ensure_ascii=False, indent=4)
        print("爬取%s条" % (t))
    db.commit()
    db.close()
