# 未# 1.写函数,要求传入列表或者元组,取得下标为偶数的值作为新的列表或者元组,返回给调用者
# def lt(l):
#     t = []
#     for i in range(len(l)):
#         if i % 2 == 0:
#             t.append(l[i])
#     l = t
#     return l
# a = [1,2,3,4]
# print(lt(a))

# 2.写函数,判断用户传入的对象(字符串,列表,元组)长度是否大于5
# def pd(l):
#     if len(l) > 5:
#         a = print("大于5")
#     else:
#         a = print("小于5")
#     return a
# a = pd("123456")
# a = pd([1,2,3])
# a = pd({1:"2",})
# 3.写函数,检查列表的长度,如果大于5,则将列表的前5项内容返回给调用者
# def pd(l):
#     if len(l) > 5:
#         return l[0:4]
# b = pd([1,2,3])
# b = pd([1,2,3,4,5,6,7])
# print(b)
# 4.写函数,要求传入一个字符串,统计每个字符出现的次数,将其制作为字典返回给调用者
# def tz(l):
#     aa = []
#     bb = list(l)
#     for i in bb:
#         if i not in aa:
#             aa.append(i)
#     l = aa
#     s = l
#     t = []
#     b = []
#     for i in range(len(bb)):
#         t.append(bb.count(bb[i]))
#     for i in range(len(s)):
#         a = {}
#         a["name"] = s[i:i + 1]
#         a["ps"] = t[i:i + 1]
#         b.append(a)
#     return b
# a = tz("asfafsfsdfsafsaffads")
# print(a)

# 5.写函数,接收三个参数,返回值较大的那个数字
# def bj(a,b,c):
#     x = 0
#     if a > b :
#         x = a
#     else :
#         x = b
#     if c > x :
#         x = c
#     return x
# a = bj(33,55,22)
# print(a)
# 6.写函数,检查传入字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容,并组合为新字典返回给调用者
# 例如:
# 传入:
# 	dic = {'k1': 'v1v2','k2': [11,22,33,44]}
# 返回:
# 	dic {'k1': 'v1','k2': [11,22]}
# 假定value只能是列表或者字符串
# def pd(dic):
#     t = []
#     print(dic.values())
#     for v in dic.values():
#         if len(v) > 2:
#             t.append(v)
#     s = []
#     for i in range(len(t)):
#         s.append(t[i][0:2])
#     dic["k1"] = s[0]
#     dic["k2"] = s[1]
#     return dic
# a = {'k1': 'v1v2','k2': [11,22,33,44]}
# print(pd(a))
# 比名片系统难一些(所有知识点的整合,列表,字符串,字典)
#
# 双色球彩票系统: 6个功能全部封装成函数.
#
# # 自己的余额自己设置
# price = 10000
#
# [{'red': 红球列表,'blue': 蓝球},{'red': 红球列表,'blue': 蓝球}]
#
# 彩票: {
# 	'red': [],
# 	'blue': int
# }
#
# 一张彩票:
# {'red': [],'blue': int}
#
# 所有的彩票:[{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int},{'red': [],'blue': int}]
#
#
# - 从1-33共33个红色号码球中选择6个号码，并从1-16共16个蓝色号码球中选择1个号码
#
# 	- 交互大框架 （原始金额自定，彩票2元一张）
# ==================================================
#    双色球 V0.01
# #  1. 充值  （先显示原有金额，再输入金额，最后显示充值后的金额）
# def cz():
#     price = 10000
#     n = int(input("请输入金额:"))
#     s = price + n
#     print("原有金额:%s  输入金额:%s  充值后金额:%s" % (price, n, s))
#
# #  2. 随机生成一个彩票 (显示生成的彩票: 红球: 12... 蓝球: 蓝球号码)
# def sc():
#     import random
#     c = []
#     z = []
#     b = random.randint(1, 16)
#     while True:
#         aa = {}
#         a = random.randint(1, 33)
#         if len(c) == 6:
#             break
#         else:
#             if a not in c:
#                 c.append(a)
#     aa["red"] = c
#     aa["blue"] = b
#     z.append(aa)
#     print("红球:%s    蓝球:%s" % (c, b))
#     print(z)
#
# #  3. 手动输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): 1,2,3,4,5,6,7
# def sr():
#     s = []
#     z = []
#     c = []
#     while True:
#         try:
#             aa = {}
#             if len(s) == 7:
#                 break
#             else:
#                 hm = input("请输入彩票号码:")
#                 if int(hm) > 33 or int(hm) < 1:
#                     print("请输入1-33的数字!!!")
#                 elif len(s) == 6:
#                     if int(hm) < 1 or int(hm) > 16:
#                         print("请输入1-16的数字!!!")
#                     else:
#                         s.append(hm)
#                         b = hm
#                 elif hm not in s:
#                     s.append(hm)
#                     c.append(int(hm))
#                 else:
#                     print("输入已存在,请重新输入!!!")
#         except Exception as e:
#             print("请输入数字!!!",e)
#     aa["red"] = c
#     aa["blue"] = b
#     z.append(aa)
#     print(z)
#     return z
#
# #  4.查看最新一期彩票结果, 显示开奖后的账户余额 （最新一期彩票结果随机产生）
# #  	格式:
# #  	本期彩票的结果为: 红球: 1,2,3,4,5,6 蓝球: 1
# #  	中6+1 奖金1000万
# #  	中5+0 奖金200
# #  	...
# #  	...
# #  	...
# #  	最终账户余额为: xxxx
# def ck():
#     print("本期彩票的结果为:")
#     sc()
#     print("最终账户余额为:")
#     cz()
#
# #  5. 显示当前余额
# def dq():
#     print("当前余额为:")
#     cz()
#
# #  6. 显示所有的彩票:
# #  			红球: 6个数字  蓝球: 1
# #  			红球: 6个数字  蓝球: 1
# #  			红球: 6个数字  蓝球: 1
# #  			红球: 6个数字  蓝球: 1
# #  			红球: 6个数字  蓝球: 1
# def sy():
#     z = []
#     while True:
#         z.append(sc())
#         if len(z) == 16:
#             break
#
# #  7.	退出系统
# def tc():
#     exit()
# # ==================================================
# #     请输入操作序号:
#
#
# a = """
# ==================================================
# #    双色球 V0.01
# 1.充值（先显示原有金额，再输入金额，最后显示充值后的金额）
# 2.随机生成一个彩票(显示生成的彩票: 红球: 12... 蓝球: 蓝球号码)
# 3.手动输入彩票号码(总共输入7个号码,每个号码中间逗号隔开,前六个是红球号码,最后一个是蓝球号码): 1,2,3,4,5,6,7
# 4.查看最新一期彩票结果, 显示开奖后的账户余额 （最新一期彩票结果随机产生）
# 5.显示当前余额
# 6.显示所有的彩票:
# 7.退出系统
# ==================================================
# """
# print(a)
# pd = int(input("请输入操作序号:"))
# while True:
#     if pd == 1:
#         cz()
#         pd = int(input("请输入操作序号:"))
#     if pd == 2:
#         sc()
#         pd = int(input("请输入操作序号:"))
#     if pd == 3:
#         sr()
#         pd = int(input("请输入操作序号:"))
#     if pd == 4:
#         ck()
#         pd = int(input("请输入操作序号:"))
#     if pd == 5:
#         dq()
#         pd = int(input("请输入操作序号:"))
#     if pd == 6:
#         sy()
#         pd = int(input("请输入操作序号:"))
#     if pd == 7:
#         tc()



