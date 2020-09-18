# score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# 1.查询score列表中成绩是满分的所有的学生学号
# score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# count = -1
# a = score.count(100)
# for i in range(a) :
#     count = score.index(100,count + 1)
#     print(count,end="\t")

# score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# c = -1
# a = score.count(100)
# for b in range(a):
#     c = score.index(100,c + 1)
#     print(c,end="\t")

# 2删除score列表中所有的数值100
# score = [68, 87, 92, 100,100, 76,100,100, 88,100, 54, 89, 76, 61]
# count = score.count(100)
# for i in range(count):
#     score.remove(100)
# print(score)

# a = []
# for i in score:
#     if i not in a:
#         a.append(i)
# a.pop(a.index(100))
# print(a)

# 3.有一个字符串,凡是出现"|"和 " "和 "-"和"," 前后,就算一个单词. 计算下列字符串  str = "hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and" 单词的个数
# str ="hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# str = str.replace("|"," ").replace("-"," ").replace(","," ")
# count = str.count(" ") + 1
# print(count)

# str ="hello world,a|nd python or and ddd and hello hello world and python or and dd-dddd and,hello wo|rld and python or and ddd and wor-ld and py-thon or and ddd and an|d ddd and"
# c = "|-,"
# for i in range(len(c)):
#     str = str.split(c[i])
#     str = " ".join(str)
# str = str.split()
# str = len(str)
# print("单词的个数为:%s"%(str))

# 4.编写程序，完成以下要求：
# 	-  统计字符串中，各个字符的个数
# 	-  比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
# a = "hello world"
# b= []
# for i in a:
#     if i not in b and i != " ":
#         count = a.count(i)
#         b.append(i)
#         print("%s:%s"%(i,count),end="\t")

# a = "hello world"
# b = []
# for i in a:
#     if i not in b and i != " ":
#         b.append(i)
#         count = a.count(i)
#         print("%s:%s"%(i,count),end="\t")





# 5.给定一个带文件后缀名的字符串,要求: 将后缀名输出来 例如:  aasd.sad.sas.da?sdasdsaa.txt  --> txt
# a = input("请输入文件名:")
# b = a.rindex(".")
# for i in range(b + 1,len(a)):
#     print(a[i],end="")

# a = input("请输入文件名:")
# a = a.split(".")
# print(a[len(a) - 1])

# 6.用户输入一堆字符串,打印出最后一个单词的长度 asdsa adasd asdsadas asdsadeasd asdsad
# a = input("请输入字符串:")
# a =a.split()
# print(len(a[len(a) - 1]))

# a = input("请输入字符串:")
# c=""
# b = a.rfind(" ")
# if  a.rfind(" ") != -1:
#     for i in range(b + 1,len(a)):
#         c += a[i]
#     print("最后一个单词为:%s" % (c))
#     print("最后一个单词长度为:%s" % (len(c)))
# else:
#     print("最后一个单词为:%s" % (a))
#     print("最后一个单词长度为:%s" % (len(a)))

# 7.用for循环打印一个菱形. 用center()做
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
# for i in range(1,12,2):
#     a = "*" * i
#     print(a.center(11))
# for i in range(9,0,-2):
#     a = "*" * i
#     print(a.center(11))

# j = 13
# for i in range(1,12,2):
#     a = "*" * i
#     b = a.center(j+i)
#     print(b)
#     j -= 2
# j = 5
# for i in range(9,0,-2):
#     a = "*" * i
#     b = a.center(j+i)
#     print(b)
#     j += 2

# 8.要求用户输入字符串,计算一个字符串中所有英文字母的个数.'dsaas12312asdas12312dsadsadsadas'
# n = input("请输入字符串:")
# s = 0
# for i in range(len(n)):
#     if ord(n[i]) >= ord("a") and ord(n[i]) <= ord("z") or ord(n[i]) >= ord("A") and ord(n[i]) <= ord("z"):
#         s += 1
# print("所有英文个数为:%s"%(s))

# 9.模拟游戏聊天框,用户能一直输入内容,按回车,打印出用户输入的内容,但是,如果输入的内容当中,有敏感词汇,替换为 *
# 敏感词汇为:  ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
#
# 示例:
# 用户输入的内容为: 你是sb吗?你大爷的,做个人吧
#
# 打印的内容为: 你是**吗?***的,做个人吧
# a = input("请输入聊天内容:")
# b = ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
# for i in b:
#     if i in a:
#         a = a.replace(i,"*" * len(i))
# print(a)

# n = input("请输入聊天内容:")
# a = ['sb','SB','sB','Sb','苍老师','你大爷','尼玛','马化腾']
# for i in range(len(a)):
#     n = n.replace(a[i],"*" * len(a[i]))
# print(n)

# 附加:
#
# 10.已知字符串 a = “aAsmr3idd4bgs7Dlsf9eAF”,要求如下
# 	- 请将a字符串的大写改为小写，小写改为大写。
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# print(a.swapcase())

# a = "aAsmr3idd4bgs7Dlsf9eAF"
# a = a.swapcase()
# print(a)
# 	- 请将a字符串的数字取出，并输出成一个新的字符串。
# s = ""
# for i in range(len(a)):
#     if ord(a[i]) >= ord("0") and ord(a[i]) <= ord("9"):
#         s += a[i]
# print("新字符串为:%s"%(s))
# 	- 请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabb’，经过去除后，输出 ‘abc’
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b =[]
# c =""
# for i in a:
#     if i not in b:
#         b.append(i)
#         c += i
# print(c)

# b =""
# for i in range(len(a)):
#     if a[i] not in b:
#         b += a[i]
# print(b)
# 	- 请将a字符串反转并输出。例：’abc’的反转是’cba’
# for i in range(len(a)-1,-1,-1):
#     b += a[i]
# print(b)

# 	- 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）(难)
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b =""
# for i in a:
#     if i >= "A" and i <= "Z" or i >= "a" and i <= "z":
#         b += i
# result = ""
# for i in range(65,91):
#     upper = chr(i) * b.count(chr(i))
#     lower = chr(i + 32) * b.count(chr(i + 32))
#     result += upper + lower
# print("排序前的字符串为:%s"%(b))
# print("排序后的字符串为:%s"%(result))

# 	- 请判断 ‘boy’里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b = "boy"
# f = True
# for i in range(len(b)):
#     for j in range(len(a)):
#         if b[i] not in a[j]:
#             f = False
#             break
# print(f)
# 	- 输出a字符串出现频率最高的字母
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# max = 0
# for i in a:
#     if a.count(i) > max:
#         max = a.count(i)
# print(max)
# b =[]
# for i in a:
#     if max == a.count(i) and i not in b:
#         b.append(i)
#         print(i)


# 11.题目描述：
# 密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。
# 假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。
# 他是这么变换的，大家都知道手机上的字母： 1–1， abc–2, def–3, ghi–4, jkl–5, mno–6, pqrs–7, tuv–8 wxyz–9, 0–0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换
# 声明：
# 密码中没有空格,不能有标点符号，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
# 输入描述:
# 输入包括多个测试数据。输入是一个明文，密码长度不超过100个字符，输入直到文件结尾；
# 输出描述:
# 输出渊子真正的密文
# 示例1：
# 输入：YUANzhi1987
# 输出：zvbo9441987
# abc–2, def–3, ghi–4, jkl–5, mno–6, pqrs–7, tuv–8 wxyz–9
# import string
# a = "YUANzhi1987"
# print("加密前的密码:%s"%(a))
# for i in a:
#     if i in "abc":
#         a = a.replace(i,"2")
#     if i in "def":
#         a = a.replace(i,"3")
#     if i in "ghi":
#         a = a.replace(i,"4")
#     if i in "jkl":
#         a = a.replace(i,"5")
#     if i in "mno":
#         a = a.replace(i,"6")
#     if i in "pqrs":
#         a = a.replace(i,"7")
#     if i in "tuv":
#         a = a.replace(i,"8")
#     if i in "wxyz":
#         a = a.replace(i,"9")
# a = a.lower()
# result = ""
# for i in a:
#     if ord(i) >= 97 and ord(i) <= 121:
#         result += chr(ord(i) + 1)
#     elif ord(i) == 122:
#         result += i
#     elif i not in string.punctuation :
#         result += i
# print("加密后的密码:%s"%(result))

# import string
# a = "YUANzhi1987"
# print("加密前的密码:%s"%(a))
# b = [["abc","2"], ["def","3"], ["ghi","4"], ["jkl","5"],["mno","6"], ["pqrs","7"], ["tuv","8"], ["wxyz","9"]]
# for i in a:
#     for j in range(len(b)):
#         if i in b[j][0]:
#             a = a.replace(i,b[j][1])
# a = a.lower()
# result =""
# for i in a:
#     if ord(i) >= 97 and ord(i) <= 121:
#         result += chr(ord(i) + 1)
#     elif ord(i) == 122:
#         result += i
#     elif i not in string.punctuation :
#         result += i
# print("加密后的密码:%s"%(result))

