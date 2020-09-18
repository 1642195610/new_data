import requests
from lxml import etree
import os
import re
os.mkdir("王者荣耀")
url = "https://pvp.qq.com/web201605/herolist.shtml"
h = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
response = requests.get(url,headers= h)
response.encoding="gbk"
response = etree.HTML(response.text)
response = response.xpath('//div//ul[@class="herolist clearfix"]/li')
for hero in response:
    m_herourl = hero.xpath('./a/@href')[0]
    m_herourl = "https://pvp.qq.com/web201605/%s"%(m_herourl)
    m_heroname = hero.xpath('./a/img/@alt')[0]
    wjjm_heroname = "王者荣耀/" + m_heroname
    os.mkdir(wjjm_heroname)
    mresponse = requests.get(m_herourl,headers = h)
    mresponse.encoding="gbk"
    mresponse = mresponse.text
    mm = etree.HTML(mresponse)
    m = mm.xpath('//div//div[@class="pic-pf"]/ul/@data-imgname')
    mnurl = mm.xpath('//div[@class="wrapper"]/div[@class="zk-con1 zk-con"]/@style')
    lmnurl = str(mnurl).find("'")
    rmnurl = str(mnurl).rfind("'")
    mnurl = str(mnurl)[lmnurl + 1:rmnurl]
    hz = mnurl.rfind(".")
    q = mnurl[:hz - 1]
    hz = mnurl[hz:]
    m = str(m).replace("&","")
    m = m.replace("['","")
    m = m.replace("']","")
    m = m.split("|")
    for mn in range(len(m)):
        mnurl = "https:" + q + str( mn + 1 ) + hz
        mnname = m[mn]
        eresponse = requests.get(mnurl,headers = h)
        emnname = wjjm_heroname + "/" + mnname + hz
        with open(emnname,"wb")as file:
            file = file.write(eresponse.content)
        print("%s下载完成"%(mnname))
    print("%s下载结束"%(m_heroname))
    print("-------------------------------------------")

