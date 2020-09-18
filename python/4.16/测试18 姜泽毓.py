# 1.使用xpath解析站酷,要求10页数据 (requests)
from lxml import etree
import requests
import csv
import h
import save
# header_csv = ["图片地址","作品名字","作品类型","人气数","评论数","点赞数","作者图案","作者"]
# with open("18 姜泽毓.csv","w",encoding="utf-8-sig",newline="") as file:
#     file_csv = csv.DictWriter(file,header_csv)
#     file_csv.writeheader()
# def save(file_name,content=None):
#     import csv
#     header_csv = ["图片地址", "作品名字", "作品类型", "人气数", "评论数", "点赞数", "作者图案", "作者"]
#     if content == None:
#         with open(file_name, "w", encoding="utf-8-sig", newline="") as data:
#             data = csv.DictWriter(data, header_csv)
#             data.writeheader()
#     else:
#         with open(file_name, "a", encoding="utf-8-sig", newline="") as data:
#             data = csv.DictWriter(data, header_csv)
#             data.writerow(content)

def pq(j,t):
    url = "https://www.zcool.com.cn/?"
    params = {
        "p": j
    }
    response = requests.get(url, headers=h.h, params=params)
    html = etree.HTML(response.text)
    m = html.xpath('//div//div[@class="card-box"]')
    def shu(rqs):
        if len(rqs) == 0:
            rqs = "无"
        else:
            rqs = rqs[0]
        return rqs
    for i in m:
        t += 1
        url = i.xpath('./div//a[@class="card-img-hover"]/img/@src')
        url = shu(url)
        mz = i.xpath('./div//a[@class="card-img-hover"]/img/@title')
        mz = shu(mz)
        lx = i.xpath('.//p[@class="card-info-type"]/@title')
        lx = shu(lx)
        rqs = i.xpath('.//span[@class="statistics-view"]/text()')
        rqs = shu(rqs)
        pls = i.xpath('.//span[@class="statistics-comment"]/text()')
        pls = shu(pls)
        dzs = i.xpath('.//span[@class="statistics-tuijian"]/text()')
        dzs = shu(dzs)
        ta = i.xpath('.//div[@class="card-item"]//img/@src')
        ta = shu(ta)
        zz = i.xpath('.//div[@class="card-item"]//a/@title')
        zz = shu(zz)
        dict = {
            "图片地址": url,
            "作品名字": mz,
            "作品类型": lx,
            "人气数": rqs,
            "评论数": pls,
            "点赞数": dzs,
            "作者图案": ta,
            "作者": zz
        }
        save.save = ("测试18.csv",dict)
        # with open("18 姜泽毓.csv", "a", encoding="utf-8-sig", newline="") as file:
        #     file_csv = csv.DictWriter(file, header_csv)
        #     file_csv.writerow(dict)
        print("爬取%s条" % (t * j))
t = 0
save.save = ("测试18.csv")
for j in range(1,11):
    print("第%s页开始"%(j))
    pq(j,t)
    print("第%s页结束"%(j))

# 2.自己实现一个翻译功能: http://www.iciba.com/
# (自己找接口,自己测试参数,自己测试请求头)
# import requests
# import h
# from lxml import etree
# dic = input("请输入需要翻译的内容:")
# url = "http://www.iciba.com/" + dic
# response = requests.get(url,headers = h.h)
# html = etree.HTML(response.text)
# m = html.xpath('//div//ul[@class="base-list switch_part"]/li')
# for i in m:
#     lx = i.xpath('./span/text()')[0]
#     x = i.xpath('./p/span/text()')
#     print(lx,x)

