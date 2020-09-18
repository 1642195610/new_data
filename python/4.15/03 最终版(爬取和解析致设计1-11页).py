from lxml import etree
import urllib.request
import urllib.parse
import csv
t = 0
header_csv = ["图片地址","作品名字","作品类型","人气数","点赞数","评论数","作者图片","作者"]
with open("3.csv","w",encoding="utf-8-sig",newline="") as data:
    data_csv = csv.DictWriter(data,header_csv)
    data_csv.writeheader()
for j in range(1,12):
    print("第%s页开始" % (j))
    url = "https://www.zhisheji.com/new_index_tj"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
    dict = {
        "page": j
    }
    a = urllib.parse.urlencode(dict).encode()
    request = urllib.request.Request(url, headers=header, data=a)
    response = urllib.request.urlopen(request)
    str = response.read().decode()
    html = etree.HTML(str)
    m = html.xpath('//ul[@class="list"]/li')
    for i in m:
        t += 1
        url = i.xpath('.//span/img/@src')[0]
        mz = i.xpath('.//span/img/@alt')[0]
        lx = i.xpath('./div[@class="desc"]/text()')
        if len(lx) > 0:
            lx = lx[0]
        else:
            lx = "无"
        rqs, dzs, pls = i.xpath('.//em/text()')
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
        with open("3.csv", "a", encoding="utf-8-sig", newline="")as data:
            data_csv = csv.DictWriter(data, header_csv)
            data_csv.writerow(dic)
        print("爬取%s条"%(t))
    print("第%s页结束"%(j))