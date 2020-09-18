from lxml import etree
import requests
import csv
from save import save
from save.save import h
import os
# os.mkdir("image")
def pq(j,t):
    url = "https://www.zcool.com.cn/?"
    params = {
        "p": j
    }
    response = requests.get(url, headers=save.h(), params=params)
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
        wn = "image/" + zz
        # os.mkdir(wn)
        ej = i.xpath('./div[@class="card-img"]/a/@href')[0]
        ejresponse = requests.get(ej, headers=save.h())
        ejhtml = etree.HTML(ejresponse.text)
        ejm = ejhtml.xpath('//div[@class="reveal-work-wrap text-center"]//img/@src')
        for img in ejm:
            murlr = requests.get(img,headers = save.h())
            mmzs = img.rfind("/")
            mmzn = img[mmzs:]
            xmmzn = wn + mmzn
            print(wn,mmzn)
            break
            # with open(xmmzn,"wb")as f:
            #     f.write(murlr.content)
            # print("下载完成")
        ejm = ",".join(ejm)
        def ejshu(rqs):
            if len(rqs) == 0:
                rqs = "无"
            return rqs
        ejm = ejshu(ejm)
        dict = {
            "图片地址": url,
            "作品名字": mz,
            "作品类型": lx,
            "人气数": rqs,
            "评论数": pls,
            "点赞数": dzs,
            "作者图案": ta,
            "作者": zz,
            "二级图片地址" : ejm
        }
        # save.save(file,dict)
        print("爬取%s条" % (t * j))
t = 0
file = "二级.csv"
# save.save(file)
for j in range(1,2):
    print("第%s页开始"%(j))
    pq(j,t)
    print("第%s页结束"%(j))
