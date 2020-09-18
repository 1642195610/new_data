# 简单题目:
# 1.编写求和函数,要求如下:
# 	格式:
# 		sum(1,100) --> 5050
# 		sum(1,100,2) --> 奇数和
# 		sum(100,1000,2) --> 奇数和
#实现sum
# def sumz(a,b,c = 1):
#     s = 0
#     for i in range(a,b + 1,c):
#         s += i
#     return s
# print(sumz(1,100))
# print(sumz(1,100,2))

# 2.实现内置函数: len()
#实现len
# def lenz(l):
#     s = 0
#     for i in l:
#         s += 1
#     return s
# print(lenz("1234s"))
# print(lenz([1,2,3,4]))
# print(lenz({1:"2",2:"3"}))
# print(lenz((1,2)))

# 3.实现内置函数: min(),max(),sum()
#实现min
# def minz(*args):
#     mi = []
#     for i in args:
#         if i not in mi:
#             mi.append(i)
#     mn = mi[0]
#     for i in mi:
#         if mn > i:
#             mn = i
#     return mn
# print(minz(1))
# print(minz(2,3,4,5,6,5,6,7,1,-3))

#实现max
# def maxz(*args):
#     ma = []
#     for i in args:
#         if i not in ma:
#             ma.append(i)
#     mx = ma[0]
#     for i in ma:
#         if mx < i:
#             mx = i
#     return mx
# print(maxz(1))
# print(maxz(2,3,4,5,6,5,6,7,1,-3))

#实现sum
# def sumz(l):
#     s = 0
#     for i in l:
#         s += i
#     return s
# print(sumz([1,2,3,4]))
# print(sumz([3,2,4,6]))


# 4.写函数,返回一个扑克牌列表,里面有52项,每一项是一个元组
# 例如:
# 	[('红心','A'),('草花','A'),...,('方块','K'),('黑桃','K')]
#
# 第一个参数: ['红心','草花','方块','黑桃']
#
# 第二个参数: ['A','2','3','4',...,'K']
# def pkp():
#     a = ["红心", "草花", "方块", "黑桃"]
#     b = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     z = []
#     for i in b:
#         for j in a:
#             c = (j, i)
#             z.append(c)
#     return z
# print(pkp())

# 笔试题目:
# 1.编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.
# 元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所
# 有数.
# def cacluate(*args):
#     s = 0
#     dy = []
#     for i in args:
#         s += i
#     s = s / len(args)
#     for i in args:
#         if i > s:
#             dy.append(i)
#     z = (s, dy)
#     return z
# print(cacluate(1,2,3,4,5))

# 2.编写一个函数, 接收字符串参数, 返回一个元组,‘ehllo WROLD’
# 元组的第一个值为大写字母的个数, 第二个值为小写字母个数.
# def dx(a):
#     d = 0
#     x = 0
#     for i in a:
#         if ord(i) >= ord("a") and ord(i) <= ord("z"):
#             x += 1
#         if ord(i) >= ord("A") and ord(i) <= ord("Z"):
#             d += 1
#     z = (d, x)
#     return z
# a = "ehllo WROLD"
# print(dx(a))

# 3.编写函数, 接收一个列表(包含30个1~100之间的随机整形数)和一
# 个整形数k, 返回一个新列表.
# 函数需求:
# - 将列表下标k之前对应(不包含k)的元素逆序;
# - 将下标k及之后的元素逆序;
# [1,2,3,4,5] 2 [2,1,5,4,3]
# def nx(a):
#     print(a)
#     pd = a[-1:-2:-1][0]
#     qn = []
#     hn = []
#     z = []
#     for i in range(len(a[0])):
#         if i < pd:
#             qn.append(a[0][i])
#         else:
#             hn.append(a[0][i])
#     qn = qn[-1::-1]
#     hn = hn[-1::-1]
#     z = qn + hn
#     return z
# a = [[1,2,3,4,5],2]
# print(nx(a))

# 4.腾讯笔试题:
# 题目需求:
# 	f(n): 返回n里面的每一位数字的平方和
#     对于一个十进制的正整数， 定义f(n)为其各位数字的平方和，如:
#     f(13) = 1**2 + 3**2 = 10
#     f(207) = 2**2 + 0**2 + 7**2 = 53
#     下面给出三个正整数k，a, b,你需要计算有多少个正整数n满足a<=n<=b,
#     且k*f(n)=n
# 输入:
#     第一行包含3个正整数k，a, b, k>=1,  a,b<=10**18, a<=b;
# 输出：
#     输出对应的答案;
#
# 范例:
#     输入: 51 5000 10000
#     输出: 3 (这些数字n具体是哪些)
# def f(n):
#     a= n
#     s = 0
#     a = list(str(a))
#     for i in a:
#         s += int(i) * int(i)
#     return s
# def pf(k,a,b):
#     t = 0
#     aa = []
#     bb = []
#     for n in range(a, b + 1):
#         if n >= a and n <= b and k * f(n) == n:
#             aa.append(n)
#             t += 1
#     bb.append(t)
#     bb.append(aa)
#     return bb
# a = pf(51,5000,10000)
# print(a)
# print(51 * f(7293))
# print(51 * f(7854))
# print(51 * f(7905))
