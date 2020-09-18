import requests
from bc.bc import sj_User_Agent,bccsv

from lxml import etree
import os
import time
import random
from lxml import etree
import csv
import json
import pymysql
db = pymysql.connect("localhost","root","","yy")
cursor = db.cursor()
def w():
    while True:
        try:
            url = "http://sc.chinaz.com/"
            header = sj_User_Agent()
            response = requests.get(url, headers=header)
            # print(response)
            response.encoding = "utf-8"
            # with open("素材.html", "w", encoding="utf-8")as file:
            #     file = file.write(response.text)
            return response.text
            break
        except Exception as e:
            print("这个请求头不可用!!!")

# with open("素材.html", "r", encoding="utf-8")as yifile:
#     yifile = yifile.read()

def url_l(a):
    yifile = a
    yifile = etree.HTML(yifile)
    w = "http://sc.chinaz.com"
    url_list = []
    mz = []
    #矢量
    sl = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[1]/text()')[0]
    su = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[1]/@href')[0]
    su = w + su
    url_list.append(su)
    mz.append(sl)
    # 高清图片
    gq = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[2]/text()')[0]
    gu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[2]/@href')[0]
    gu = w + gu
    url_list.append(gu)
    mz.append(gq)
    # 图标
    tb = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[3]/text()')[0]
    tu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[3]/@href')[0]
    tu = w + tu
    url_list.append(tu)
    mz.append(tb)
    # PSD素材
    psd = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[4]/text()')[0]
    pu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos"]/a[4]/@href')[0]
    pu = w + pu
    url_list.append(pu)
    mz.append(psd)
    #字体
    zt = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no2"]/a[1]/text()')[0]
    zu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no2"]/a[1]/@href')[0]
    url_list.append(zu)
    mz.append(zt)
    # 英文字体
    yw = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no2"]/a[3]/text()')[0]
    ywu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no2"]/a[3]/@href')[0]
    url_list.append(ywu)
    mz.append(yw)
    # 音效
    yx = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no2"]/a[4]/text()')[0]
    yxu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no2"]/a[4]/@href')[0]
    yxu = w + yxu
    url_list.append(yxu)
    mz.append(yx)
    # PPT模板
    ppt = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no3"]/a[3]/text()')[0]
    ppu = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no3"]/a[3]/@href')[0]
    ppu = w + ppu
    url_list.append(ppu)
    mz.append(ppt)
    # 简历模板
    jl = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no3"]/a[4]/text()')[0]
    ju = yifile.xpath('//div//div[@class="nav"]/ul/li[@class="nos no3"]/a[4]/@href')[0]
    ju = w + ju
    url_list.append(ju)
    mz.append(jl)
    # print(sl,su,gq,gu,tb,tu,psd,pu,zt,zu,yw,ywu,yx,yxu,ppt,ppu,jl,ju,url_list,mz)
    return [url_list,mz]

# os.mkdir("html")
# for m in range(len(url_list)):
#     sj = random.randint(1,5)
#     time.sleep(sj)
#     mresponse = requests.get(url_list[m], headers = sj_User_Agent())
#     print(mresponse)
#     mresponse.encoding="utf-8"
#     s = "html/" + mz[m] +".html"
#     print(s)
#     with open(s, "w", encoding="utf-8")as file:
#         mfile = file.write(mresponse.text)
header_csv = ['矢量', '高清图片', '图标', 'PSD素材', '字体', '英文字体', '音效', 'PPT模板', '简历模板']
filename = "素材.csv"
with open(filename, "w", encoding="utf-8-sig",newline="")as csv_file:
    csv_file = csv.DictWriter(csv_file,header_csv)
    csv_file.writeheader()
list = []
def we(j):
    filename = "素材.csv"
    t = 0
    for m in range(len(url_l(w())[0])):
        t += 1
        s = "html/" + url_l(w())[1][m] + ".html"
        # print(s)
        # with open(s, "r", encoding="utf-8")as file:
        #     mfile = file.read()
        sj = random.randint(1, 3)
        time.sleep(sj)
        urll = url_l(w())[0][m]
        mresponse = requests.get(urll, headers=sj_User_Agent())
        mresponse.encoding = "utf-8"
        mfile = etree.HTML(mresponse.text)
        def hh(m):
            if m + 1 == 1:
                # 矢量
                sl_url = mfile.xpath('//div//div[@class="text_left"]//div[@class="box picblock col3"]/div/a/img/@src2')
                # for m in sl_url:
                #     return m
                return sl_url
            elif m + 1 == 2:
                # 高清图片
                tp_url = mfile.xpath('//div[@id="container"]/div[@class="box picblock col3"]/div/a/img/@src2')
                # for m in tp_url:
                #     return m
                return tp_url
            elif m + 1 == 3:
                # 图标
                tb_url = mfile.xpath('//ul[@class="pngblock imgload"]/li/p/a/img/@src2')
                # for m in tb_url:
                #     return m
                return tb_url
            elif m + 1 == 4:
                # PSD素材
                psd_url = mfile.xpath('//div[@class="box col3 ws_block"]/a/img/@src')
                # for m in psd_url:
                #     return m
                return psd_url
            elif m + 1 == 5:
                # 字体
                zt_url = mfile.xpath('//div//div[@class="index_font_list clearfix"]//li[@class="font"]/div/a/img/@src')
                # for m in zt_url:
                #     return m
                return zt_url
            elif m + 1 == 6:
                # 英文字体
                ywzt_url = mfile.xpath('//li[@class="font"]/div/a/img/@src')
                # for m in ywzt_url:
                #     return m
                return ywzt_url
            elif m + 1 == 7:
                # 音效
                yx_url = mfile.xpath('//div[@class="music_block"]/p[@class="n1"]/@thumb')
                # for m in yx_url:
                #     return m
                return yx_url
            elif m + 1 == 8:
                # PPT模板
                ppt_url = mfile.xpath('//div[@class="sc_warp  mt20"]/div[@id="main"]/div/div/a/img/@src')
                # for m in ppt_url:
                #     return m
                return ppt_url
            elif m + 1 == 9:
                # 简历模板
                jl_url = mfile.xpath('//div[@class="sc_warp  mt20"]/div[@id="main"]/div/div/a/img/@src')
                # for m in jl_url:
                #     return m
                return jl_url
            else:
                pass
        dic = {
            '矢量': hh(m),
            '高清图片': hh(m),
            '图标': hh(m),
            'PSD素材': hh(m),
            '字体': hh(m),
            '英文字体': hh(m),
            '音效': hh(m),
            'PPT模板': hh(m),
            '简历模板': hh(m)
        }
        # print(dic)
        list.append(dic)
        bccsv(filename,dic)
        hh = ",".join(hh(m))
        print(hh,type(hh))
        sql = "insert into sc (矢量,高清图片,图标,PSD素材,字体,英文字体,音效,PPT模板,简历模板) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        hh, hh, hh, hh, hh, hh, str(hh), hh, hh)
        cursor.execute(sql)
        with open("素材.json", "w", encoding="utf-8")as json_file:
            json_file = json.dump({"total": t * j, "data": list}, json_file, ensure_ascii=False, indent=4)
        print("爬取%s条"%(t))
for i in range(1,120):
    print("第%s页开始"%(i))
    we(i)
    print("第%s页结束" % (i))
db.commit()
db.close()
