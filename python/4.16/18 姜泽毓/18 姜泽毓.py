# 1.下载英雄联盟英雄的皮肤图片: (要求每个英雄都有一个文件夹,文件夹是该英雄的名字,文件夹里面的图片文件就是这个英雄的皮肤)
# 	https://lol.qq.com/data/info-heros.shtml
import requests
from save.save import h
import json
import os
# url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
# response = requests.get(url , headers = h())
# response = response.text
# response = json.loads(response)
# # os.mkdir("image")
# for i in response["hero"]:
#     m = i["heroId"]
#     print("%s英雄图片下载开始"%(i["name"]))
#     wjjn = "image/" + i["name"]
#     # os.mkdir(wjjn)
#     eurl = "https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js"%(m)
#     eresponse = requests.get(eurl,headers = h())
#     for ie in eresponse.json()["skins"]:
#         if ie["chromas"] == "0":
#             xmn = ie["name"]
#             xmurl = ie["mainImg"]
#             xm = xmurl.rfind(".")
#             xmh = xmurl[xm:]
#             xmtn = wjjn + "/" + xmn.replace("/"," ") + xmh
#             xmurlr = requests.get(xmurl, headers=h())
#             # with open(xmtn,"wb")as file:
#             #     file.write(xmurlr.content)
#             print("%s下载完成" % (xmn))
#     print("%s英雄图片下载结束" % (i["name"]))
#     print("------------------------------------------")

# 2.下载简历模板: (站长素材)
# 	http://sc.chinaz.com/jianli/free.html
from lxml import etree
# # os.mkdir("18 姜泽毓")
# url = "http://sc.chinaz.com/jianli/index_3.html"
# response = requests.get(url , headers = h())
# response = response.content.decode()
# html = etree.HTML(response)
# m = html.xpath('//div//div[@id="container"]/div/a/@href')
# for i in m:
#     urlm = i
#     eresponse = requests.get(urlm,headers = h())
#     eresponse = eresponse.content.decode()
#     meresponse = etree.HTML(eresponse)
#     eresponse = meresponse.xpath('//div//div[@class="bgwhite"]//h1/text()')[0]
#     wjjn ="18 姜泽毓/" + eresponse
#     os.mkdir(wjjn)
#     wj = meresponse.xpath('//div//div[@id="down"]//div[@class="clearfix mt20 downlist"]/ul[@class="clearfix"]/li/a/@href')[0]
#     hz = wj.rfind(".")
#     hzm = wj[hz:]
#     wjnm = wjjn + "/" + eresponse + hzm
#     wjnmurl = requests.get(wj,headers = h())
#     with open(wjnm,"wb")as file:
#         file = file.write(wjnmurl.content)
#     print("%s下载成功" % (eresponse))

# 3.自己找一个图片网站(比如百度图片..),下载海量图片
#
# (按照自己在网页中的操作找出接口)
# 王者荣耀文件夹:https://pvp.qq.com/web201605/herolist.shtml
# os.mkdir("王者荣耀文件夹")
# url = "https://pvp.qq.com/web201605/herolist.shtml"
# response = requests.get(url , headers = h())
# response.encoding="utf-8"
# response = response.content.decode("gbk")
# response = etree.HTML(response)
# response = response.xpath('//div//ul[@class="herolist clearfix"]/li')
# t = 0
# print("下载开始")
# for i in response:
#     murl = i.xpath('./a/img/@src')[0]
#     mn = i.xpath('./a/img/@alt')[0]
#     murl = "https:%s"%(murl)
#     ii = murl.rfind(".")
#     hz = murl[ii:]
#     mn = "王者荣耀文件夹/" + mn + hz
#     mresponse = requests.get(murl,headers = h())
#     with open(mn,"wb")as file:
#         file = file.write(mresponse.content)
#     t += 1
#     print("下载%s张完成"%(t))
#     print("下载结束")
