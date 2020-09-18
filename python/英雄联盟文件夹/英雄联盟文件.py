import requests
import json
import os
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
h = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
response = requests.get(url , headers = h)
response = response.text
response = json.loads(response)
os.mkdir("英雄联盟")
for i in response["hero"]:
    m = i["heroId"]
    print("%s英雄图片下载开始"%(i["name"]))
    wjjn = "英雄联盟/" + i["name"]
    os.mkdir(wjjn)
    eurl = "https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js"%(m)
    eresponse = requests.get(eurl,headers = h)
    for ie in eresponse.json()["skins"]:
        if ie["chromas"] == "0":
            xmn = ie["name"]
            xmurl = ie["mainImg"]
            xm = xmurl.rfind(".")
            xmh = xmurl[xm:]
            xmtn = wjjn + "/" + xmn.replace("/"," ") + xmh
            xmurlr = requests.get(xmurl, headers=h)
            with open(xmtn,"wb")as file:
                file.write(xmurlr.content)
            print("%s下载完成" % (xmn))
    print("%s英雄图片下载结束" % (i["name"]))
    print("------------------------------------------")

