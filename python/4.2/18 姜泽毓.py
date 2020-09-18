# 0.
# 任意选取豆瓣电影top250的5条数据用数据类型表示出来(汪峰, 字典和列表的组合
# 列表包5个字典)
# 肖申克的救赎
# 肖申克的救赎  / The Shawshank Redemption  / 月黑高飞(港) / 刺激1995(台) [可播放]
# 导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...
# 1994 / 美国 / 犯罪 剧情
#
#  9.7 1956099人评价
# 希望让人自由。
#
# 2霸王别姬
# 霸王别姬  / 再见，我的妾 / Farewell My Concubine [可播放]
# 导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...
# 1993 / 中国大陆 中国香港 / 剧情 爱情 同性
#
#  9.6 1444228人评价
# 风华绝代。
#
# 3阿甘正传
# 阿甘正传  / Forrest Gump  / 福雷斯特·冈普 [可播放]
# 导演: 罗伯特·泽米吉斯 Robert Zemeckis   主演: 汤姆·汉克斯 Tom Hanks / ...
# 1994 / 美国 / 剧情 爱情
#
#  9.5 1484955人评价
# 一部美国近现代史。
#
# 4这个杀手不太冷
# 这个杀手不太冷  / Léon  / 杀手莱昂 / 终极追杀令(台)
# 导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...
# 1994 / 法国 / 剧情 动作 犯罪
#
#  9.4 1679349人评价
# 怪蜀黍和小萝莉不得不说的故事。
#
# 5美丽人生
# 美丽人生  / La vita è bella  / 一个快乐的传说(港) / Life Is Beautiful
# 导演: 罗伯托·贝尼尼 Roberto Benigni   主演: 罗伯托·贝尼尼 Roberto Beni...
# 1997 / 意大利 / 剧情 喜剧 爱情 战争
#
#  9.5 937934人评价
# 最美的谎言。
# a = [{
#     "name":"1肖申克的救赎",
#     #别名
#     "alias":"/ The Shawshank Redemption  / 月黑高飞(港) / 刺激1995(台) [可播放]",
#     # 导演
#     "director":"弗兰克·德拉邦特 Frank Darabont",
#     #主演
#     "To star":["蒂姆·罗宾斯","Tim Robbins"],
#     "year":"1994 / 美国 / 犯罪 剧情",
#     #评分
#     "score":"9.7",
#     #评分人数
#     "Score number":"1956099人评价",
#     #简介
#     "brief introduction":"希望让人自由。"
# },{
#     "name":"2霸王别姬",
#     #别名
#     "alias":"/ 再见，我的妾 / Farewell My Concubine [可播放]",
#     # 导演
#     "director":"陈凯歌 Kaige Chen",
#     #主演
#     "To star":["张国荣","Leslie Cheung","张丰毅","Fengyi Zha"],
#     "year":"1993 / 中国大陆 中国香港 / 剧情 爱情 同性",
#     #评分
#     "score":"9.6",
#     #评分人数
#     "Score number":"1444228人评价",
#     #简介
#     "brief introduction":"风华绝代。"
# },{
#     "name":"3阿甘正传",
#     #别名
#     "alias":"/ Forrest Gump  / 福雷斯特·冈普 [可播放]",
#     # 导演
#     "director":["罗伯特·泽米吉斯","Robert","Zemeckis"],
#     #主演
#     "To star":"汤姆·汉克斯 Tom Hanks / ...",
#     "year":"1994 / 美国 / 剧情 爱情",
#     #评分
#     "score":"9.5",
#     #评分人数
#     "Score number":"1484955人评价",
#     #简介
#     "brief introduction":"一部美国近现代史。"
# },{
#     "name":"4这个杀手不太冷",
#     #别名
#     "alias":"/ Léon  / 杀手莱昂 / 终极追杀令(台)",
#     # 导演
#     "director":"吕克·贝松 Luc Besson",
#     #主演
#     "To star":["让·雷诺","Jean Reno","娜塔莉·波特曼"],
#     "year":"1994 / 法国 / 剧情 动作 犯罪",
#     #评分
#     "score":"9.4",
#     #评分人数
#     "Score number":"1679349人评价",
#     #简介
#     "brief introduction":"怪蜀黍和小萝莉不得不说的故事。"
# },{
#     "name":"5美丽人生",
#     #别名
#     "alias":"/ La vita è bella  / 一个快乐的传说(港) / Life Is Beautiful",
#     # 导演
#     "director":"罗伯托·贝尼尼 Roberto Benigni",
#     #主演
#     "To star":["罗伯托·贝尼尼","Roberto","Beni"],
#     "year":"1997 / 意大利 / 剧情 喜剧 爱情 战争",
#     #评分
#     "score":"9.5",
#     #评分人数
#     "Score number":"937934人评价",
#     #简介
#     "brief introduction":"最美的谎言。"
# }]

# 1.
# 有字符串
# "key1:1|key2:2|key3:3|key4:5"
# 处理成字典
# {'key1': 1, 'key2': 2...}
# a = "key1:1|key2:2|key3:3|key4:5"
# a = ":".join(a.split("|")).split(":")
# print(a)
# b = {}
# for i in range(0,len(a),2):
#     b[a[i]] = a[i + 1]
# print(b)

# 2.
# 有列表a = [11, 77, 22, 33, 88, 44, 55, 77, 88, 70, 30, 99], 将所有大于60的值保存在字典的第一个key中, 将小于60的值保存在第二个key中:
# 格式: {'key1': 大于60的值列表, 'key2': 小于60的值列表}
# a = [11, 77, 22, 33, 88, 44, 55, 77, 88, 70, 30, 99]
# da = []
# xiao = []
# for i in a :
#     if i > 60:
#         da.append(i)
#     else:
#         xiao.append(i)
# z = {'key1':da, 'key2':xiao}
# print(z)
# a = [11, 77, 22, 33, 88, 44, 55, 77, 88, 70, 30, 99]
# b = ["key1","key2"]
# a.sort(reverse=True)
# s = []
# c = {}
# d = []
# sd = []
# for i in a:
#     if i > 60 :
#         s.append(i)
#     else:
#         d.append(i)
# sd.append(s)
# sd.append(d)
# for i in range(len(b)):
#     c[b[i]] =sd[i]
# print(c)

# 3.
# 输出商品列表, 用户输入序号, 显示用户选中的商品
# 商品列表:
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],
#             ['wife', 10], ['wifi', 100000]]
# a.把商品列表变为:
# products = [{'name': 'iphone8', 'price': 6888}, {'name': 'MacPro', 'price': 14888}, {'name': '小米6', 'price': 2499},
#             {'name': 'Coffe', 'price': 31}....]
productss = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],
            ['wife', 10], ['wifi', 100000]]
b = []
for k,v in productss:
    a = {"name":k,"price":v}
    b.append(a)
print(b)
# list_ = []
# for i in range(len(productss)):
#     products = {}
#     products["name"] = productss[i][0]
#     products["price"] = productss[i][1]
#     list_.append(products)
# print(list_)

# b.在a的基础上, 页面显示: 序号 + 商品名称 + 商品价格:

# 1
# iphone8
# 6888
# 2
# MacPro
# 14888
# 3
# 小米6
# 2499
# list_ = []
# a =list(range(1,9))
# for i in range(len(productss)):
#     products = {}
#     products["serial_number"] = a[i]
#     products["name"] = productss[i][0]
#     products["price"] = productss[i][1]
#     list_.append(products)
#     aa = products["serial_number"]
#     ab = products["name"]
#     ac = products["price"]
#     print("%s  %s  %s"%(aa,ab,ac))
# c.用户输入商品的序号, 打印商品名称和价格
# list_ = []
# a =list(range(1,9))
# for i in range(len(productss)):
#     products = {}
#     products["serial_number"] = a[i]
#     products["name"] = productss[i][0]
#     products["price"] = productss[i][1]
#     list_.append(products)
#     aa = products["serial_number"]
#     ab = products["name"]
#     ac = products["price"]
# f = False
# while True:
#     try:
#         if f == False:
#             for i in range(len(list_)):
#                 b = int(input("请输入商品序号:"))
#                 print(list_[b - 1]["name"], list_[b - 1]["price"])
#                 f = True
#                 break
#         else:
#             break
#     except:
#         print("请输入数字!!!")
# d.如果用户输入的商品序号有误(没有该商品), 提示输入有误, 并重新输入
# list_ = []
# a =list(range(1,9))
# for i in range(len(productss)):
#     products = {}
#     products["serial_number"] = a[i]
#     products["name"] = productss[i][0]
#     products["price"] = productss[i][1]
#     list_.append(products)
#     aa = products["serial_number"]
#     ab = products["name"]
#     ac = products["price"]
# f = False
# while True:
#     try:
#         if f == False:
#             for i in range(len(list_)):
#                 b = int(input("请输入商品序号:"))
#                 if b in a:
#                     print(list_[b - 1]["name"], list_[b - 1]["price"])
#                     f = True
#                     break
#                 else:
#                     print("输入有误,没有该商品请重新输入:")
#         else:
#             break
#     except:
#         print("请输入数字!!!")
# e.用户输入Q或者q, 退出程序
# list_ = []
# a =list(range(1,9))
# for i in range(len(productss)):
#     products = {}
#     products["serial_number"] = a[i]
#     products["name"] = productss[i][0]
#     products["price"] = productss[i][1]
#     list_.append(products)
#     aa = products["serial_number"]
#     ab = products["name"]
#     ac = products["price"]
# f = False
# while True:
#     try:
#         if f == False:
#             for i in range(len(list_)):
#                 b = int(input("请输入商品序号:"))
#                 if b in a:
#                     print(list_[b - 1]["name"], list_[b - 1]["price"])
#                     f = True
#                     break
#                 b = str(b)
#                 print(b)
#                 if b == "q" or b == "Q":
#                     f = True
#                     break
#                 b = int(b)
#                 if b not in a:
#                     print("输入有误,没有该商品请重新输入:")
#         else:
#             break
#     except:
#         print("请输入数字!!!")
# 4.
# 电影投票, 由用户给每个电影打分, 最终显示每个电影的评分(用户输入分数);
# 电影列表: list = ['囧妈', '疯狂的外星人', '金瓶梅', '战狼', '哪吒传奇', '灵魂摆渡']
#
# 格式如下:
# 请给囧妈打分: 8
# 请给疯狂的外星人打分: 10
# ...
# ...
#
# 显示的结果:
# {'囧妈': 8, '疯狂的外星人': 10...}
#
# 5.
# 车牌区域计数:
# 所有的车牌号:
# cars = ['京A88888', '赣B12345', '沪C76543', '黑B33445', '京B22445', '沪A67854', '黑C67890']
#
# locals = {'沪': '上海', '黑': '黑龙江', '赣': '江西', '京': '北京'}
#
# 运行结果为:
# {'黑龙江': 2, '上海': 2, '北京': 2, '江西': 1}
#
# 6.
# zhubo = {'卢本伟': 5000000, '冯提莫': 8888, 'UZI': 8000000000, 'mlxg': 1000000, 'letme': 88888888, '张琪格': 1000, '陈一发': 50000}
# a.计算主播的平均收益
# b.删除利益小于平均值的主播
#
# 7.
# 根据以下字典, 把数字的发音读出来
# dic = {
#     '-': 'fu',
#     '0': 'ling',
#     '1': 'yi',
#     '2': 'er',
#     '3': 'san',
#     '4': 'si',
#     '5': 'wu',
#     '6': 'liu',
#     '7': 'qi',
#     '8': 'ba',
#     '9': 'jiu',
#     '.': 'dian'
# }
# 运行:
# 请输入一个数: -328
# 发音为: fu
# san
# er
# ba
# def dic() :
#     dic = {
#      '-': 'fu',
#      '0': 'ling',
#      '1': 'yi',
#      '2': 'er',
#      '3': 'san',
#      '4': 'si',
#      '5': 'wu',
#      '6': 'liu',
#      '7': 'qi',
#      '8': 'ba',
#      '9': 'jiu',
#      '.': 'dian'
#      }
#     return dic
# print(dic())
# a = input("请输入一个数:")
# print("发音为:",end=" ")
# for i in range(len(a)):
#     for j in dic():
#         if a[i] == j:
#             print(dic()[j])
# 8.
# 思考题(仅做思考, 能实现最好!!!): 对于第7题, 假如要求读出:
# 请输入一个数: -328
# 发音为: fu
# san
# 百
# er
# 十
# ba
# def dic() :
#     dic = {
#      '-': 'fu',
#      '0': 'ling',
#      '1': 'yi',
#      '2': 'er',
#      '3': 'san',
#      '4': 'si',
#      '5': 'wu',
#      '6': 'liu',
#      '7': 'qi',
#      '8': 'ba',
#      '9': 'jiu',
#      '.': 'dian'
#      }
#     return dic
# def w() :
#     b = {
#         "1":"",
#         "2": "十",
#         "3": "百",
#         "4": "千",
#         "5": "万",
#         "6": "十万",
#         "7": "百万",
#         "8": "千万",
#         "9": "亿",
#         "10": "十亿",
#         "11": "百亿",
#         "12": "千亿",
#         "13": "万亿"
#     }
#     return b
# a = input("请输入一个数:")
# print("发音为:",end=" ")
# sz_list =[]
# for i in range((len(a))):
#     #调用函数dic()
#     for j in dic():
#         if a[i] == j:
#             sz_list.append(dic()[j])
# #取出的是数字
# wei_list = []
# for i in range(len(a)):
#     for k in w():
#         if str(len(a) - i) == k:
#             # 取出的是位数,例如:百位,十位...
#             wei_list.append(w()[k])
# #判断是负数还是正数
# if a[0] == "-":
#     wei_list.pop(0)
#     wei_list.insert(0,"")
# z = []
# #合并数字和位数
# for i in range(len(sz_list)):
#     z.append(sz_list[i] + wei_list[i])
# z ="".join(z)
# print(z)
# 输入一个数: 1234
# 发音为: yi
# 千
# er
# 百
# san
# 十
# si
#
# 9.
# 写函数, 传入一个参数n, 返回n的阶乘的结果
# 例如: cal(5)
# 返回的结果为: 5 * 4 * 3 * 2 * 1
# def jc(n):
#     s = 1
#     for i in range(1,n + 1):
#         s *= i
#     return s
# a = jc(5)
# print(a)
# 10.
# 写函数, 要求函数传两个参数(n, m), 返回给调用者一个结果, 结果为n - m的和
# def s(n,m):
#     sum = 0
#     for i in range(n,m + 1):
#         sum += i
#     return sum
# a = s(1,100)
# print(a)
# 例: b = sum(1, 100)
# b = 5050
#
# 11.
# 写函数, 要求函数传入三个参数, 返回这三个参数的最大值
# def m(a,b,c):
#     max = 0
#     if a > b :
#         max = a
#     else:
#         max = b
#     if max < c:
#         max = c
#     return max
# a = m(1,2,3)
# print(a)
# 例: b = max(10, 30, 40)
# b = 40
#
# 12.
# 写函数, 实现一个列表去重的功能, 要求传入一个列表, 给调用者返回一个去重以后的列表
# def l(list) :
#     a = []
#     for i in list:
#         if i not in a:
#             a.append(i)
#     return a
# a = l([1,2,3,4,5,1,2,3,4,1,23,4,4])
# print(a)
# 例: b = quchong([11, 22, 33, 44, 55, 11, 33])
# b = [11, 22, 33, 44, 55]
#
# - 名片管理系统(不考虑重复)
#
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# 名片管理系统
# def x():
#     a =["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤"]
#     return a
# def m():
#     a = ["涵清","星舞","秋枫","晨月","霁华","烟霏","殷云","烟岚","霏微","夕佳","思邈","紫琪","雅君","涵","鸿月","茜","雅洁","语彤","梓璇","靖怡","倾哥","清浅","疏影","茗月","醉烟","月墨","云落","桂燕","子琴", "腊梅", "芬", "莉娅", "娟娣", "艳红", "棠莉" ,"悦驰" ,"婉婷", "嘉洁" ,"彩红", "媛雪", "美芳", "束芳", "淑琳", "若瑶","莉轩", "燕齐", "昕妍", "思思" ,"玉瑶" ,"子婧" ,"爱琴", "维娟", "思娜", "欢欢" ,"鸾瑶" ,"玲丽", "旦娅", "苏娟" ,"宝琳" ,"思念","羽洁", "秋艳", "建颖" ,"泓茹", "富霞", "倩成" ,"诗茹" ,"欣瑶", "曦秀", "婷丽", "莉娜" ,"东玲" ,"巧娜" ,"佳艳" ,"蓓莉" ,"纪颖"]
#     return a
# def dz():
#     a = ["北京", "上海", "广州", "深圳", "辽宁", "天津", "四川", "广西", "山东", "山西", "西安", "云南", "新疆", "呼和浩特", "包头", "赤峰", "鄂尔多斯","呼伦贝尔", "阿拉善盟", "济南", "青岛", "烟台", "威海", "潍坊", "德州", "滨州", "东营", "聊城", "菏泽", "临沂", "北京", "上海", "天津", "重庆","淄博", "泰安", "枣庄", "日照", "莱芜", "海阳", "平度", "莱阳", "石家庄", "沧州", "承德", "秦皇岛", "唐山", "保定", "廊坊", "邢台", "衡水"]
#     return a
# V0
# .01
# 1.
# 添加一个新的名片
# 2.
# 删除一个名片(先查找, 是否删除)
# 3.
# 修改一个名片(先查找, 是否修改)
# 4.
# 查询一个名片
# 5.
# 显示所有的名片(50
# 条) [{}, {}, {}]
# import random
# list_mp = []
# for i in range(50):
#     mp = {}
#     mp["name"] = x()[random.randint(0,50)] + m()[random.randint(0,50)]
#     mp["QQ"] = random.randint(1000000000,10000000000)
#     mp["wxh"] = random.randint(10000000000,100000000000)
#     mp["add"] = dz()[random.randint(0,50)]
#     list_mp.append(mp)
# print(list_mp)
# 6.
# 退出系统
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# 每条数据都应该有: 姓名, QQ号, 微信号, 住址
#
# -  QQ(10
# 位随机数)
# - 微信(11
# 位随机数)
# - 纯数字
# - 默认的50条数据在程序运行的时候随机产生
# 请输入操作序号: 5
# aaa
# 8909
# weixin
# 北京
# bbb
# 9099
# weixin
# 上海
# - 增:
# - 请输入名字, qq, 微信, 住址
# - 删
# - 请输入要删除的名字
# - 改(先查询, 再更新)
# - 请输入要修改的名字: 请输入名字, qq, 微信, 住址
#
# - 查询某一个人的数据:
# - 请输入要查询的名字:
#
#
#
