with open("2.html","r",encoding="utf-8")as file:
    file = file.read()
from lxml import etree
import csv
html = etree.HTML(file)
m = html.xpath('//ul[@class="list"]/li')
t = 0
header_csv = ["图片地址", "作品名字", "作品类型", "人气数", "点赞数", "评论数", "作者图片", "作者"]
with open("2.csv", "a", encoding="utf-8-sig", newline="")as data:
    data_csv = csv.DictWriter(data, header_csv)
    data_csv.writeheader()
for i in m:
    t += 1
    url = i.xpath('.//span/img/@src')[0]
    mz = i.xpath('.//span/img/@alt')[0]
    lx = i.xpath('./div[@class="desc"]/text()')
    if len(lx) > 0 :
        lx = lx[0]
    else:
        lx = "无"
    rqs,dzs,pls = i.xpath('.//em/text()')
    ta = i.xpath('.//a/img/@src')[0]
    zz = i.xpath('.//a/img/@alt')[0]
    dic = {
        "图片地址": url,
        "作品名字": mz,
        "作品类型": lx,
        "人气数": rqs,
        "点赞数": dzs,
        "评论数": pls,
        "作者图片": ta,
        "作者": zz
    }
    with open("2.csv", "a", encoding="utf-8-sig", newline="")as data:
        data_csv = csv.DictWriter(data, header_csv)
        data_csv.writerow(dic)
