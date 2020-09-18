# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# # 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)
# import random
# a = []
# while len(a) != 6:
#     b = random.randint(1,33)
#     if b not in a:
#         a.append(b)
# a.append(random.randint(1,16))
# print(a)

# import random
# #创建一个空列表
# a = []
# # 生成6个红色的不一样的双色球
# while len(a) != 6:
#     b = random.randint(1,33)
#     if b not in a:
#         #判断是否重复
#         a.append(b)
#         #最后生成一个蓝色的双色球
# a.append(random.randint(1,16))
# print(a)

# 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
# 1.
# import random
# n =int(input("请输入N:"))
# a = list(range(1,n + 1))
# b = random.sample(a,n)
# print(b)

# 2.
# import random
# n = int(input("请输入N:"))
# a =[]
# while len(a) != n:
#     b = random.randint(1,n)
#     if b not in a:
#         a.append(b)
# print(a)

# 2.[68, 87, 92, 100, 76, 88, 54, 89, 76, 61] 去除列表中的偶数  --> [87,89,61]
# a = [68, 87, 92, 100, 76, 88, 54, 89, 76, 61]
# c = 0
# while c < len(a):
#     if a[c] % 2 == 0:
#         a.remove(a[c])
#         c -= 1
#     c += 1
# print(a)

# import random
# n = int(input("'请输入N:"))
# a = []
# while len(a) != n:
#     b = random.randint(1,n)
#     if b not in a:
#         a.append(b)
# print(a)

# import random
# n = int(input("请输入N:"))
# 产生1-n的数并转换为列表a
# a = list(range(1,n + 1))
#随机从a列表中,取n个不重复的数放在b列表中
# b = random.sample(a,n)
# print(b)
# 1.冒泡排序(优化后)
# a = [12,3123,123,3,4,354,3]
# for i in range(len(a) -1):
#     t = False
#     for j in range(len(a) - 1 - i):
#         if a[j] > a[j + 1]:
#             t = True
#             a[j],a[j + 1] = a[j + 1],a[j]
#     print(a)

# 2.选择排序
# a = [12,3123,123,3,4,354,3]
# for i in range(len(a)):
#     for j in range(i + 1,len(a)):
#         if a[i] > a[j] :
#             a[i],a[j] = a[j],a[i]
# print(a)

# 4.请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
# [342,564,576,876,897,908,53,534,576,876,534,2354,654,6857,786,987,897]
# [[342,564,576],[876,897,908]....]
# list1 = []
# a = list(range(1,101))
# print(a)
# for i in range(len(a)):
#     if i % 3 == 0:
#         b = []
#         b.append(a[i])
#         if i + 1 < len(a):
#             b.append(a[i + 1])
#         if i + 2 < len(a):
#             b.append(a[i + 2])
#         list1.append(b)
# print(list1)

# 6.现有列表[10,123,243,256,87,10,324,654,10,234,10,342,567,10,345,10] 查找出10在列表中出现的下标
# index(10,下标 + 1)  (到底查找几次,用count方法)
# a = [10,123,243,256,87,10,324,654,10,234,10,342,567,10,345,10]
# index = -1
# 10出现的次数
# b = a.count(10)
#循环10出现的次数
# for i in range(b):
#       找到一个10 就下标+1 继续找下一个
#     index = a.index(10,index + 1)
#       找到一个就打印一个
#     print(index,end="\t")

# 8.写一个循环，不断的问用户想买什么，用户选择一个商品编号(下标)，就把对应的商品添加到购物车(列表)里，最终用户输入q退出时，打印购物车里的商品列表. 数据
# # products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
# # 结果: 输出买的所有商品名字,格式为:
# # 	你购买的商品为: iphone8: 个数(count)	MacPro:个数...
# # 	总价为: xx元
# # 价格和商品名字一一对应

products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
sum = 0
sp = []
while True:
	a = input("请输入要购买的序号:")
	try:
		if a == "q" or a == "Q":
			break
		elif int(a) in range(len(products)):
			i = int(a)
			xq = products[i][1]
			sum += xq
			xq_name =products[i][0]
			sp.append(xq_name)
		else:
			print("请输入一个正确的序号")
	except Exception as e:
		print("请输入正确的数字")
print("总价为:%s"%(sum))
new = []
print("你要购买的商品为:",end="\t")
for name in sp:
	if name not in new:
		xq_c = sp.count(name)
		new.append(name)
		print("%s: %s"%(name,xq_c),end="\t")