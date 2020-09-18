import requests
from lxml import etree
import re
import json
import csv
from bc.bc import bccsv
import random
import time
import pymysql
def nr(url,j):
    t = 0
    while True:
        try:
            header = {
                "User-Agent": "Mozilla/5.0 (Linux; U; Android 9; zh-CN; Mi9 Pro 5G Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.21.0.63 Mobile Safari/537.36 AliApp(shuqi_android/11.1.1.109) UCBS/2.11.1.1 TTID/src1075 WindVane/8.5.0 Shuqi (Xiaomi-Mi9 Pro 5G__shuqi__11.1.1.109__1075) AliApp(SQREADER/11.1.1.109)"
            }
            sj = random.randint(1, 10)
            time.sleep(sj)
            response = requests.get(url, headers=header)
            response = etree.HTML(response.text)
            m = response.xpath('//div[@id="app"]//div[@class="item"]')
            ur = response.xpath('//body[@data-spm="page_render_sq_bookstore_k94b7ann"]/script[2]/text()')
            ur = str(ur[0])
            p = r'window.__INITIAL_STATE__=(.+);(.+?);'
            urz = re.findall(p, ur, re.S)[0][0]
            p = r'(.+?);.+?'
            urz = re.findall(p, urz, re.S)[:2]
            urz = urz[0] + urz[1]
            urd = json.loads(urz, encoding="utf-8")
            urd = urd["modulesInfos"][1]["data"]["books"]
            for i in range(len(urd)):
                t += 1
                # 字数
                zishu = urd[i]["wordCount"]
                # 分类
                fenlei = urd[i]["className"]
                # 书名
                shuming = urd[i]["bookName"]
                # 书号
                shuhao = urd[i]["bookId"]
                # 封面图片地址
                surl = urd[i]["imgUrl"]
                # 作者
                zz = urd[i]["authorName"]
                # 标签
                biaoqian = urd[i]["tag"]
                biaoqian = ",".join(biaoqian)
                # 开始时间
                kaishi = urd[i]["startTime"]
                # 结束时间
                jieshu = urd[i]["endTime"]
                # 描述
                miaoshu = urd[i]["desc"]
                miaoshu = miaoshu.replace("\n", "").replace(" ", "").replace("......","").replace("'","")
                # print(zishu,fenlei,shuming,shuhao,surl,zz,biaoqian,kaishi,jieshu,miaoshu)
                dict = {
                    "字数": zishu,
                    "分类": fenlei,
                    "书名": shuming,
                    "书号": shuhao,
                    "封面图片地址": surl,
                    "作者": zz,
                    "标签": biaoqian,
                    "开始时间": kaishi,
                    "结束时间": jieshu,
                    "描述": miaoshu
                }
                list.append(dict)
                bccsv(filename, dict)
                with open("书旗小说.json", "w",encoding="utf-8")as file_json:
                    file_json = json.dump({"total":t * j,"data":list}, file_json, ensure_ascii=False, indent=4)
                sql = "insert into sqxs (字数,分类,书名,书号,封面图片地址,作者,标签,开始时间,结束时间,描述) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%((zishu,fenlei,shuming,shuhao,surl,zz,biaoqian,kaishi,jieshu,miaoshu))
                cursor.execute(sql)
                print("爬取%s条"%(t))
            if t == len(urd):
                break
        except Exception as e:
            print("换页,错误%s"%(e))
filename = "书旗小说.csv"
header_csv = ['字数', '分类', '书名', '书号', '封面图片地址', '作者', '标签', '开始时间', '结束时间', '描述']
with open(filename, "w", encoding="utf-8-sig", newline="")as file_csv:
    file_csv = csv.DictWriter(file_csv, header_csv)
    file_csv.writeheader()
db = pymysql.connect("localhost","root","","书旗小说")
cursor = db.cursor()
list = []
for j in range(1,51):
    print("第%s页开始"%(j))
    url = "https://render-web.shuqireader.com/render/sq-bookstore/page/k94b7ann/?appfunction=an_bmk,1_clo,1_smjs,1&soft_id=%s&ver=200422&subVer=sqrelease&appVer=11.1.1.109&platform=an&placeid=1075&imei=860204041846236&oaid=72407613d9d7db24&sdk=28&wh=1080x2135&msv=3&enc=023361587608482712&sn=1587608069965182&vc=eef7&mod=Mi9+Pro+5G&manufacturer=Xiaomi&brand=Xiaomi&net_type=wifi&first_placeid=src1075&aak=158d5e&user_id=1719605275&utype=pre_vip&net=4&net_env=4&coreType=1&rom=9&skinId=999&skinVersion=1.0&skinVersionPrefix=1&imagetype=1&utdid=WElPaG04aHgzbG9EQUJlQmNVZ0JLTVlG&umidtoken=a8tLPAJLOtHzxjVxpHrYct+p0NA1K5qX&permissionType=3&writer_switch=1&serviceWorkerOn=1&spm=a2oun.page_render_sq_bookstore_k94b2r2m.WxBookListN_13_1.module HTTP/1.1"%(j)
    nr(url,j)
    print("第%s页结束"%(j))
db.commit()
db.close()
