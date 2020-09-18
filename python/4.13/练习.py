import urllib.request
url = "https://www.zhisheji.com/space-uid-95009.html"
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request)
srt_data = response.read().decode()
with open("测试.html", "w", encoding="utf-8")as file:
    file = file.write(srt_data)
with open("测试.html","r",encoding="utf-8") as data :
    data = data.read()
p = r'<li id=".+?">(.+?)</div>\s+</li>'
import re
tp = re.findall(p,data,re.S)
z = []
for i in tp:
    p = r'<span class="img-box"><img class="previews" mysrc="" src="(.+?)" alt="(.+?)"'
    tu = re.findall(p,i,re.S)[0]
    url = tu[0]
    mz = tu[1]
    p =r'<span class="img-box"><img class="previews" mysrc="" src=".+?" alt="(.+?)"'
    zp = re.findall(p,i,re.S)[0]
    p = r'<em><span class="icon-view"></span>(.+?)</em>'
    rqs = re.findall(p,i,re.S)[0]
    p = r'<em><span class="icon-praise"></span>(.+?)</em>'
    dzs = re.findall(p,i,re.S)[0]
    p = r'<em><span class="icon-comment"></span>(.+?)</em>'
    pls = re.findall(p,i,re.S)[0]
    dic = {
        "图片地址":url,
        "作品名字":mz,
        "作品类型":zp,
        "人气数":rqs,
        "点赞数":dzs,
        "评论数":pls
    }
    z.append(dic)
import csv
header = ["图片地址","作品名字","作品类型","人气数","点赞数","评论数"]
with open("测试.csv","w",encoding="utf-8-sig",newline="")as data:
    data_csv = csv.DictWriter(data,header)
    data_csv.writeheader()
    data_csv.writerows(z)
    
