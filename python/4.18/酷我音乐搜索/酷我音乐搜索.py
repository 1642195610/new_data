import requests
import os
import tkinter.messagebox as tm
from tkinter import *
a = Tk()
def ss():
    info = ""
    url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord"
    s = a1.get()
    if s != "":
        params = {
            "key": s,
            "pn": "",
            "rn": "30",
            "reqId": "b7da5490-812a-11ea-aca5-4b67fef3455a"
        }
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            "Referer": "http://www.kuwo.cn/search/list?key=%E9%82%93%E7%B4%AB%E6%A3%8B",
            "csrf": "OVGNCODZGJ8",
            "Host": "www.kuwo.cn",
            "Cookie": "_ga=GA1.2.1086436030.1587030968; _gid=GA1.2.665045569.1587172030; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1587030968,1587172030,1587176680,1587182965; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1587182965; _gat=1; kw_token=OVGNCODZGJ8"
        }
        response = requests.get(url, headers=header, params=params)
        all = response.json()["data"]["list"]
        os.mkdir(s)
        t = 0
        for m in all:
            t += 1
            gqm = m["name"]
            if gqm != "":
                bh = m["rid"]
                murl = "http://www.kuwo.cn/url?format=mp3&rid=%s&response=url&type=convert_url3&br=128kmp3&from=web&t=1587184246434&reqId=5f85ff30-812d-11ea-aca5-4b67fef3455a" % (
                    bh)
                mheader = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
                mresponse = requests.get(murl, headers=mheader)
                myurl = mresponse.json()["url"]
                hzs = myurl.rfind(".")
                hz = myurl[hzs:]
                myn = s + "/" + gqm + hz
                myresponse = requests.get(myurl, headers=mheader)
                with open(myn, "wb")as file:
                    file = file.write(myresponse.content)
                info += "%s首(%s)下载完成" % (t, gqm) + "\r"
        tm.showinfo(s, info)
        info += "%s下载结束" % (s)
        info += "---------------------------------------------"
a1 = Entry(a)
l1 = Label(a,text = "请输入你要搜索的<歌手名字>或者是<歌曲名字>:",font = ("华文行楷",15)).grid(row = 0)
b = Tk()
Label(b, text="输入内容按<确定>按钮,请稍等,直到弹窗出现,就下载完成啦!!!",width =90 ,height = 15,bg = "black",fg = "red",font = ("华文行楷",30)).pack()
a1.grid(row = 0 , column = 1)
Button(a,text = "确定",command = ss,font = ("华文行楷",15)).grid(row = 2 , column = 1)
Button(a,text = "退出",command = a.quit,font = ("华文行楷",15)).grid(row = 2,column = 0)
a.mainloop()