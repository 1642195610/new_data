# url = 'https://www.baidu.com/s?a=10&b=20&c=哈哈哈&d=呵呵呵'
# url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=aaa&rsv_t=09a3HQ2Jo94VNQ74K%2FRVX6otC7zBGUwJPB5HkQAsObZJWjGJYDPl8cqz%2BuU&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=1200&rsv_sug4=1201"
# a = []
# b = {}
# a = " ".join(" ".join(" ".join(url.split("?")).split("&")).split("=")).split(" ")
# a= a[1:]
# print(a)
# for i in range(0,len(a),2):
#         b[a[i]] = a[i + 1]
# print(b)

# 用户输入5个人的信息:
# 运行显示:
#
# 输入第1个人的信息:
# 姓名:   xx
# 性别:   xxx
# 年龄:xx
# 地址:xx
#
# 输入第2个人的信息:
# 姓名:
# 性别:
# 年龄:
# 地址:
#
# ....
#
# 5个人的信息输入完毕以后,按照以下格式显示5个人的信息,
#
# 姓名: xx  性别: xx  年龄: xx  地址: xx
# 姓名: xx  性别: xx  年龄: xx  地址: xx
# 姓名: xx  性别: xx  年龄: xx  地址: xx
# 姓名: xx  性别: xx  年龄: xx  地址: xx
# 姓名: xx  性别: xx  年龄: xx  地址: xx
# list = []
# for i in range(1,6):
#     tuple = {}
#     print("输入第%s个人的信息:"%(i))
#     a = input("姓名: ")
#     b = input("性别: ")
#     c = input("年龄: ")
#     d = input("地址: ")
#     print()
#     tuple = {"name":a,"sex":b,"age":c,"add":d}
#     # tuple["姓名:"] = a
#     # tuple["性别:"] = b
#     # tuple["年龄:"] = c
#     # tuple["地址:"] = d
#     list.append(tuple)
# print(list)
# for i in list:
#     a = (i["name"],i["sex"],i["age"],i["add"])
#     print("姓名: %s   性别: %s   年龄: %s   地址: %s"%a)

# a = {"n":1,"m":2,"o":3}
# for k in a.keys():
#     print(k,end="\t")
# print()
# for v in a.values():
#     print(v,end="\t")
# print()
# for k,v in a.items():
#     print(k,v,end="\t")
# print()