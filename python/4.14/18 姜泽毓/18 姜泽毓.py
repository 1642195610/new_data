#用Xpath做致设计
import urllib.request
import urllib.parse
from lxml import etree
import csv
header_csv = ["图片地址","作品名字","作品类型","人气数","点赞数","评论数","作者图片","作者"]
with open("18 姜泽毓.csv","w",encoding="utf-8-sig",newline="") as data:
    data_csv = csv.DictWriter(data,header_csv)
    data_csv.writeheader()
    t = 0
for j in range(2,12):
    url = "https://www.zhisheji.com/new_index_tj"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
    dict = {
        "page": j
    }
    a = urllib.parse.urlencode(dict).encode()
    request = urllib.request.Request(url, headers=header, data=a)
    response = urllib.request.urlopen(request)
    str_data = response.read().decode()
    html = etree.HTML(str_data)
    url = html.xpath('//span/img[@class="previews"]/@src')
    mz = html.xpath('//span/img[@class="previews"]/@alt')
    lx = html.xpath('//div[@class="desc"]/text()')
    shu = html.xpath('//div/em/text()')
    rqs = []
    for i in range(0, len(shu), 3):
        rqs.append(shu[i])
    dzs = []
    for i in range(1, len(shu), 3):
        dzs.append(shu[i])
    pls = []
    for i in range(2, len(shu), 3):
        pls.append(shu[i])
    ta = html.xpath('//div//img[@class="previews"]/@src')
    zz = html.xpath('//div//a[@target="_blank"]/@title')
    for i in range(0,len(url)):
        t += 1
        dic = {
            "图片地址": url[i],
            "作品名字": mz[i],
            "作品类型": lx[i],
            "人气数": rqs[i],
            "点赞数": dzs[i],
            "评论数": pls[i],
            "作者图片": ta[i],
            "作者": zz[i]
        }
        with open("18 姜泽毓.csv", "a", encoding="utf-8-sig", newline="")as data:
            data_csv = csv.DictWriter(data, header_csv)
            data_csv.writerow(dic)
            print("爬取%s条" % (t))
    print("第%s页结束"%(j - 1))
