# 1.	写出冒泡排序,选择排序的算法。（5分）
# 1.冒泡排序
# a = [3,5,4]
# for i in range(len(a) - 1):
#     flag = False
#     for i in range(len(a) - 1 - i):
#         if a[i] > a[i + 1]:
#             a[i],a[i + 1] = a[i + 1],a[i]
#             flag = True
#     if flag == False :
#         break
# print("最大数为%s"%(a[len(a) -1 ]))
# 2.选择排序
# a = [3,5,4]
# for i in range(len(a) - 1):
#     for j in range(i + 1,len(a)):
#         if a[i] > a[j] :
#             a[i],a[j] = a[j],a[i]
# print("最大数为%s"%(a[len(a) - 1]))

# 2.	实现一个单例（5分）
# class A:
#     i = None
#     def __new__(cls, *args, **kwargs):
#         if A.i == None:
#             A.i = super().__new__(cls, *args, **kwargs)

# 3.	给一个不低于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。（5分）
# a = 143256
# b = len(str(a))
# print("它是%s位数"%(b))
# b = str(a)
# b = [i for i in b][::-1]
# b = int("".join(b))
# print("逆序前:%s"%(a))
# print("逆序后:%s"%(b))

# 4.	鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只。(5分)
# x = 1
# while True:
#     y = 30 - x
#     if 2 * x + 4 * y == 90 :
#         break
#     else:
#         x += 1
# print("鸡有%s只,兔有%s只"%(x,y))

# 5.	控制台输出以下格式:
# 123456
# 234561
# 345612
# 456123
# 561234
# 612345
# def a ():
#     a = list(range(1,7))
#     a = str(a) * 6
#     for i in a:
#         print(i,end="")
# a()





# （10分）
#
# 6.	手动输入一个存储整数的数组，要求输出数组里面的2个最大值。
#   输入：1,2,5,9,84,3,2
#   输出：84,9（10分）
# a = input("请输入数组:").split(",")
# a = [int(i) for i in a]
# a.sort()
# print("最大的2个数为%s,%s"%(a[len(a) - 1],a[len(a) - 2]))

# 7.	将字符串"a-b-c-d-e-f"倒叙输出,中间变为大写: “f-e-d-C-b-a”（10分）
# a = "a-b-c-d-e-f"
# a = a.split("-")
# for i in range(len(a) - 1):
#     if a[i] =="c":
#         a[i] = a[i].upper()
# a = a[::-1]
# a = "-".join(a)
# print(a)

# 8.	编写一个程序，计算a + aa + aaa + aaaa的值，给定的数字作为a的值。假设为程序提供了以下输入：
# 9     然后，输出应该是： 11106（10分）
# a = 9
# s = 0
# for i in range(1,5):
#     b = str(a) * i
#     s += int(b)
# print(s)

# 9.	功能描述：删除字符串中字符个数最少的字符，最少字符串有多个，最少的要全部删除 然后返回该字符串
# 输入：asdasdas
# 输出：asasas（10分）
# a = "asdasdas"
# print("删除前:%s"%(a))
# b = ""
# for i in a:
#     if i not in b:
#         b += i
# c = {}
# for i in b :
#     c[i] = a.count(i)
# list = []
# for k,v in c.items():
#     list.extend([[k,v]])
# b = []
# for i in list:
#     b.append(i[1])
# b.sort()
# for i in list:
#     if b [0] == i[1] :
#         z = i[0]
# a = a.replace(z,"")
# print("删除后:%s"%(a))

# 10.	有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数，用代码写出来（15分）
# a=[1,2,3,4]
# list=[]
# for i in a:
#     for j in a:
#             for k in a:
#                 if i!=j and k != j and i!=k:
#                     list.append(str(i)+str(j)+str(k))
# print("共有%s种组合，分别为%s"%(len(list),list))

# 11.	用户输入日期,判断是否为日期,格式如下: 2018-12-6,年份1-9999,月份01-12或者1-12,天数01-31或者1-31,不用考虑每个月的具体天数,例如: 2018-2-31也满足（15分）
# b = input("请输入日期(例:2018-12-6):")
# a =b.split("-")
# for i in range(len(a)):
#     a[i] = int(a[i])
# flag = False
# if a[0] >= 1 and a[0] <= 9999 :
#     if a[1] >= 1 and a[1] <= 12 :
#         if a[2] >= 1 and a[2] <= 31 :
#             flag = True
# if flag == True:
#     print("%s是日期"%(b))
# else:
#     print("%s不是日期"%(b))