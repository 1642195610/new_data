# 递归题目:
#
# 1.求阶乘: f(5) --> 120  f(6) --> 720
# 	5的阶乘: 5 * 4 * 3 * 2 * 1
# 			n * f(n - 1)
# def f(n):
#     if n == 1:
#         return 1
#     return f(n - 1) * n
# print("%s"%(f(5)))
# print(f(6))

# 2.斐波那契数列: 1,1,2,3,5,8,13,21,34.... 求f(20),第20个数是多少?
# f(3): f(1) + f(2)
#
# f(4): f(3) + f(2)
#
# f(20): f(19) + f(18)
# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     return f(n - 1) + f(n - 2)
# print(f(3),f(4))
# print(f(20))

# 3.公园里有一只猴子和一堆桃子，猴子每天吃掉桃子总数的一半，把剩下一半中扔掉一个坏的。到第七天的时候，猴子睁开眼发现只剩下一个桃子。问公园里刚开始有多少个桃子？
# def tz(n):
#     if n == 1:
#         return 1
#     return (tz(n - 1) + 1) * 2
# print(tz(7))
#
# is和==
# a = 1
# b = 1
# print((a == b)) #True
# print(a is b) #True
# a = "1"
# b = "1"
# print((a == b)) #True
# print(a is b) #True

# 列表生成式
# a = [1,2,3,4,5]
# s = 0
# b = [x ** x for x in a]
# print(b)
# 值传递和引用传递
# #值传递
# a =10
# b = a
# b = 9
# print("a=",a) #a= 10
# print("b=",b) #b= 9
# #引用传递
# a = [1,2]
# b = a
# b[0] = 9
# print("a=",a) #a= [9, 2]
# print("b=",b) #b= [9, 2]

# 赋值,浅拷贝,深拷贝
#赋值
# a = [1,2,3]
# b = a
# b [0] = [9]
# print("a=",a) #a= [[9], 2, 3]
# print("b=",b) #b= [[9], 2, 3]
#浅拷贝
# import copy
# # # 1.
# a = [1,2,3]
# b = copy.copy(a)
# b [0] = [9]
# print("a=",a) #a= [1, 2, 3]
# print("b=",b) #b= [[9], 2, 3]
# # # 2.
# a = [[4,5],2,3]
# b = copy.copy(a)
# b [0][0] = [99]
# print("a=",a) #a= [[[99], 5], 2, 3]
# print("b=",b) #b= [[[99], 5], 2, 3]
#深拷贝
# import copy
# a = [[4,5],2,3]
# b = copy.deepcopy(a)
# b [0][0] = [99]
# print("a=",a) #a= [[4, 5], 2, 3]
# print("b=",b) #b= [[[99], 5], 2, 3]