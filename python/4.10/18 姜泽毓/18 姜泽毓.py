# 1.检索邮箱:
# @前面可以有字母数字下划线
# @后面都不能有下划线, 可以有数字或者字母
# 21312321 @ qq.com
# abc @ 163.com
# hwqeqewyh @ aaaedu.cc
# a @ sad.com.cc
# abc @ wqeq.org
# abc_abc @ abc.abc
# a @ 163.abc

# s = "21312321@qq.com"
# s = "abc@163.com"
# s = "hwqeqewyh@aaaedu.cc"
# s = "a@sad.com.cc"
# s = "abc@wqeq.org"
# s = "abc_abc@abc.abc"
# s = "a@163.abc"
# s = input("请输入邮箱地址:")
# import re
# g = r"^\w+@[0-9a-z]{2,6}\.[a-z]{2,3}(\.[a-z]{2,3}$)?"
# a = re.search(g,s,re.I)
# if a == None:
#     print("不是邮箱地址")
# else:
#     print("是邮箱地址")

# 2.
# 检验身份证号:
# 18位:
# 1位不能是0
# 2 - 17: 纯数字
# 18: 数字或者x

# s = input("请输入身份证号:")
# import re
# g = r"^[1-9]\d{16}[0-9x]$"
# a = re.search(g,s,re.I)
# if a == None:
#     print("不是身份证号")
# else:
#     print("是身份证号")

# 3.
# 检验手机号:
# s = input("请输入手机号:")
# import re
# g = r"^1[345789]\d{9}$"
# a = re.search(g,s,re.I)
# if a == None:
#     print("不是手机号")
# else:
#     print("是手机号")

# 4.
# 校验网址
# http: // www.baidu.com
# http: // baidu.com
# www.baidu.com
# https: // www.baidu.com
# tieba.baidu.com
# news.baidu.com
# yuan.news.baidu.com
# news.baidu.com.cn

# s = "http://www.baidu.com"
# s = "http://baidu.com"
# s = "www.baidu.com"
# s = "https://www.baidu.com"
# s = "tieba.baidu.com"
# s = "news.baidu.com"
# s = "yuan.news.baidu.com"
# s = "news.baidu.com.cn"
# s = input("请输入网址:")
# import re
# g = r"^(http(s)?://)?[a-z]{2,7}\.\w{2,7}((\.[a-z]{2,7})?\.[a-z]{2,7})?$"
# a = re.search(g,s,re.I)
# if a == None:
#     print("不是网址")
# else:
#     print("是网址")

# 5.
# 将站酷放在pycharm打开, 然后取出每条数据的
# 作品图片url地址, 作品名字, 作品类型, 人气数, 评论数, 点赞数, 作者
# 如果没有该字段的数据, 写无;
# 把数据存入到csv(4.9)
import re
import csv
with open("../../4.13/18 姜泽毓.html", "r", encoding="utf-8-sig") as file:
    file_=file.read()
    #图片URL
        #先取外层
    g = r'<div class="card-img">\s(.+?)</div>'
    file_list = re.findall(g,file_,re.S)
    file_list = "".join(file_list)
        #再取图片地址
    g = r'<img src="(.+?)"'
    file_listURL= re.findall(g,file_list,re.S)
    # print(file_listURL,len(file_listURL))
        #作品名字
    g = r'<img src="(.+?)">'
    file_listZP = re.findall(g,file_list,re.S)
    file_listZP = "".join(file_listZP)
    g=r'title="(.+?)"'
    file_listMZ = re.findall(g,file_listZP)
    # print(file_listMZ,len(file_listMZ))
        #作品类型
    g = r'<p class="card-info-type" title="(.+?)">'
    file_listLX = re.findall(g,file_,re.S)
    # print(file_listLX,len(file_listLX))
        #人气数
    g = r'<span class="statistics-view" title="共(.+?)人气">|<span class="time" title="推广">(.+?)</span>'
    file_listRQS = re.findall(g,file_,re.S)
    file_listRQS = [file_listRQS[i][0] if file_listRQS[i][0] != "" else "无" for i in range(len(file_listRQS))]
    # print(file_listRQS, len(file_listRQS))
        #评论数
    g = r'<span class="statistics-comment" title="共(.+?)评论">'
    file_listPLS = re.findall(g,file_,re.S)
    g = r'<span class="statistics-comment" title="共(.+?)评论">|<span class="time" title="推广">(.+?)</span>|<span class="statistics-product" title="(.+?)">4</span>'
    file_listPLS = re.findall(g, file_, re.S)
    file_listPLS = [file_listPLS[i][0] if file_listPLS[i][0] != "" else "无" for i in range(len(file_listPLS))]
    # print(file_listPLS,len(file_listPLS))
        #点赞数
    g = r'<span class="statistics-tuijian" title="共(.+?)推荐">|<span class="time" title="推广">(.+?)</span>'
    file_listDZS = re.findall(g,file_,re.S)
    file_listDZS = re.findall(g, file_, re.S)
    file_listDZS = [file_listDZS[i][0] if file_listDZS[i][0] != "" else "无" for i in range(len(file_listDZS))]
    # print(file_listDZS, len(file_listDZS))
        #作者
    g = r'<div class="card-item">\s(.+?)</div>'
    file_listZZ = re.findall(g,file_,re.S)
    file_listZZS = "".join(file_listZZ)
    g = r'<a href="(.+?)">'
    file_listZZSS = re.findall(g,file_listZZS)
    file_listZZSZ = "".join(file_listZZSS)
    g = r'title="(.+?)"'
    file_listZZSSS = re.findall(g,file_listZZSZ)
    # print(file_listZZSSS,len(file_listZZSSS))
    zd = []
    header = ["图片URL地址", "作品名字", "作品类型", "人气数", "评论数", "点赞数", "作者"]
    for i in range(len(file_listURL)):
        fen ={}
        fen[header[0]] = file_listURL[i]
        fen[header[1]] = file_listMZ[i]
        fen[header[2]] = file_listLX[i]
        fen[header[3]] = file_listRQS[i]
        fen[header[4]] = file_listPLS[i]
        fen[header[5]] = file_listDZS[i]
        fen[header[6]] = file_listZZSSS[i]
        zd.append(fen)
    print(zd,len(zd))
with open("18 姜泽毓.csv","w",encoding="utf-8-sig",newline="")as f:
    csv_f = csv.DictWriter(f,header)
    csv_f.writeheader()
    csv_f.writerows(zd)