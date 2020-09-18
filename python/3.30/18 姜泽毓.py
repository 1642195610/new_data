# 列表作业:
# 1.调用列表操作的常用函数实现以下功能:
# 	- 1)创建一个空列表score
# score = []
# print(score)
# 	- 2)在score列表中依次追加10个数值([68, 87, 92, 100, 76, 88, 54, 89, 76, 61] )
# 		extend()
# 		append()
# score.extend([68, 87, 92, 100, 76, 88, 54, 89, 76, 61])
# print(score)
# 	- 3)输出score列表中第3个元素的数值
# a = score[2]
# print(a)
# 	- 4)输出score列表中第1～6个元素的值
# for i in range(0,6):
    # print(score[i],end="\t")
# 	- 5)在score列表第3个元素之前添加数值59
# score.insert(2,59)
# print(score)
# 	- 6)利用变量num保存数值76，查询76分在score列表中出现的次数
# num = score.count(76)
# print(num)
# 	- 7)查询列表中是否有num76分的考试成绩
# a = score.index(76)
# print(a)
# 	- 8)查询score列表中成绩是满分的学生学号
# a = score.index(100)
# print(a)
# 	- 9)score列表中将59分加1分
# score[2] = 59 + 1
# print(score[2])
# 	- 10)删除score列表中第1个元素
# print(score)
# score.pop(0)
# print(score)
# 	- 11)获得score列表中元素的个数
# a = len(score)
# print(a)
# 	- 12)对列表中所有元素进行排序，输出考试的最高分和最低
# score.sort(reverse=True)
# print("最高分为:%s"%(score[0]))
# score.sort()
# print("最低分为:%s"%(score[0]))
# 	- 13)颠倒score列表中元素的顺序
# print(score)
# score.reverse()
# print(score)
# 	- 14)删除score列表中尾部的元素
# print(score)
# score.pop()
# print(score)
# 	- 15)score列表中追加数值88，并输出。删除score列表中第一个数值88
# print("原列表:",score)
# score.append(88)
# print("追加后:",score)
# score.pop(score.index(88))
# print("删除后:",score)
# 	- 16)创建2个列表score1和score2,score1中包含数值2个元素值80,61,score2中包含3个元素值71,95,82，合并这两个列表，并输出全部元素
# score1 = [80,61]
# score2 = [71,95,82]
# score3 = []
# for a in score1:
#     if a not in score3:
#         score3.append(a)
# for a in score2:
#     if a not in score3:
#         score3.append(a)
# print(score3)
# 	- 17)创建score1列表，其中包含数值2个元素值80,61，将score1中元素复制5遍保存在score2列表中，输出score2列表中全部元素。
# score1 = [80,61]
# score2 = score1 * 5
# print(score2)

# 2.[68, 87, 92, 100, 76, 88, 54, 89, 76, 61] 去除列表中的偶数  --> [87,89,61]
# a = [68, 87, 92, 100, 76, 88, 54, 89, 76, 61]
# b = []
# for c in a:
#     if c % 2 != 0:
#         b.append(c)
# print(b)

# 3.双色球: 红色球可以在1-33个编号中任意选择6个，蓝色球可以在1-16中选择一个
# 要求: 随机生成双色球,使用列表输出,前6个红球,最后1个是篮球 (去重,random)
# import random
# a =[]
# while True:
#     b = random.randint(1,33)
#     if b not in a:
#         a.append(b)
#     if len(a) == 6:
#         break
# print(a,end=" ")
# c =[]
# while True:
#     d = random.randint(1,33)
#     if d not in c:
#         c.append(d)
#     if len(c) == 1:
#         break
# print(c)

# 4.请写出一段 Python 代码实现分组一个 list 里面的元素, [1,2,3,...100]变成 [[1,2,3], [4,5,6]....,[97,98,99],[100]]
# 创建一个空列表
# list1=[]
# list = [100]
# # 循环 1-100
# for i in range(1,101):
#     #赋值 list1=[1,2,3......100]
#     list1.append(i)
#     #输出 list1列表
# print(list1)
# #创建空列表
# list3=[]
# # 遍历列表
# for i in list1:
# # 每3位放一个下标里
#     if i%3==0:
#         list2=[i-2,i-1,i]
#         list3.append(list2)
# list3.append(list)
# print(list3)

# 5. 用户输入n,生成含有 n 个元素值为 1~n 的列表,元素顺序随机,但值不重复:
# import random
# a = []
# n = int(input("请输入n:"))
# while True:
#     b = random.randint(1,n)
#     if b not in a:
#         a.append(b)
#     if len(a) == n:
#         break
# print(a)

# 附加题:
#
# 6.现有列表[10,123,243,256,87,10,324,654,10,234,10,342,567,10,345,10] 查找出10在列表中出现的下标  index(10,下标 + 1)  (到底查找几次,用count方法)
# a = [10,123,243,256,87,10,324,654,10,234,10,342,567,10,345,10]
# for i in range(0,len(a)):
#     if a[i] == 10:
#         print(a.index(10,i))

# 7.自己实现列表的sort方法
#   [12,3123,123,3,4,354,3] --> [3,3,4,12..]
# t = 0
# a = [12,3123,123,3,4,354,3]
# for j in range(1,7):
#     for i in range(0,len(a)-1):
#         if a[i] > a[i+1] :
#             t = a[i]
#             a[i] = a[i+1]
#             a[i+1] = t
# print(a)

# 8.写一个循环，不断的问用户想买什么，用户选择一个商品编号(下标)，就把对应的商品添加到购物车(列表)里，最终用户输入q退出时，打印购物车里的商品列表. 数据
# products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
# 结果: 输出买的所有商品名字,格式为:
# 	你购买的商品为: iphone8: 个数(count)	MacPro:个数...
# 	总价为: xx元
# 价格和商品名字一一对应
a = []
products = [['iphone8', 6888], ['MacPro', 14888], ['小米6', 2499], ['Coffe', 31], ['Book', 80], ['NIke Shoes', 799],['wife',10],['wifi',100000]]
j = [0] * len(products)
while True:
    try:
        b = input("请输入要购买的商品:")
        if b == "q" or b == "Q":
            break
        else:
            b = int(b)
            if b not in a:
                a.append(products[b])
                j[b]=(a.count(products[b]))
    except:
        print("请输入正确的序号!")
print("你购买的商品为:",end=" ")
s = 1
sum = 0
for i in range(0,len(products)):
    print("%s:%s个"%(products[i][0],j[i]),end="\t")
    s = products[i][1] * j[i]
    sum += s
print()
print("总价为:%s元"%(sum))



