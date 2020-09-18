#coding=utf-8
from lxml import etree
from bc.bc import bccsv
with open("4.html", "r", encoding="utf-8")as erfile:
    erfile = erfile.read()
# print(erfile)


def z(filename,erfile):
    erfile = etree.HTML(erfile)
    # 标题
    bt = erfile.xpath('//div[@class="main-wrap"]/div[@class="house-title"]/h1/text()')[0]
    # 浏览量
    ll = erfile.xpath('//div[@class="main-wrap"]/div[@class="house-title"]/p/em/text()')[0]
    # 图片地址
    tp = erfile.xpath('//div[@class="main-wrap"]//div[@id="bigImg"]/img[@id="smainPic"]/@src')[0]
    # 付款方式
    fk = erfile.xpath('//div[@class="main-wrap"]//div[@class="house-pay-way f16"]//span[@class="instructions"]/text()')[
        0]
    # 租赁方式
    zl = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[1]/span[2]/text()')[0]
    # 房屋类型
    fw = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[2]/span[2]/text()')[0].replace(" ", "").replace(
        "\n", "")
    # 朝向楼层
    cx = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[3]/span[2]/text()')[0].replace(" ", "").replace(
        "\n", "")
    # 所在小区
    xq = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[4]/span[2]/a/text()')[0].replace(" ", "").replace(
        "\n", "")
    # 所属区域
    qy = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[5]/span[2]/a/text()')[0].replace(" ", "").replace(
        "\n", "")
    # 详细地址
    xx = erfile.xpath('//div[@class="main-wrap"]//ul[@class="f14"]/li[6]/span[2]/text()')[0].replace(" ", "").replace(
        "\n", "")
    # print(bt,ll,tp,fk,zl,fw,cx,xq,qy,xx)
    dic = {
        "标题": bt,
        "浏览量": ll,
        "图片地址": tp,
        "付款方式": fk,
        "租赁方式": zl,
        "房屋类型": fw,
        "朝向楼层": cx,
        "所在小区": xq,
        "所属区域": qy,
        "详细地址": xx
    }
    print(dic)
    bccsv(filename, dic)
