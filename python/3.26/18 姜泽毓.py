# 1.让用户输入两个任意的整数, 比较两个数的大小, 输出最大的数
"""a=int(input("第1个整数为:"))
b=int(input("第2个整数为:"))
if a > b :
    print("最大数为:%s"%(a))
else:
    print("最大数为:%s"%(b))"""

# 2.用户输入一个数,打印出奇数还是偶数
"""a=int(input("判断数为:"))
if a % 2 == 0 :
    print("判断数为:偶数")
else:
    print("判断数为:奇数")"""

# 3.用户输入帐号密码,帐号为admin,密码为8888显示登录成功,其余的显示登录失败
"""a=input("请输入帐号:")
b=int(input("请输入密码："))
if a == "admin" and b == 8888 :
    print("登录成功")
else:
    print("登录失败")"""

# 4.用户输入一个三位数,输出结果是否为水仙花数(水仙花数: 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。)
"""a=int(input("请输入一个三位数:"))
bai=a // 100
shi=a % 100 // 10
ge=a % 10
if bai ** 3 + shi ** 3 + ge ** 3 == a :
    print("%s:是水仙花数"%(a))
else:
    print("%s:不是水仙花数"%(a))"""

# 5.用户输入年份,输出结果是闰年还是平年(闰年: 1.能整除4且不能整除100 2.能整除400)
"""a=int(input("请输入一个年份:"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("%s:是闰年"%(a))
else:
    print("%s:是平年"%(a))"""

# 6.输入公交卡当前的余额,空座位数，只要超过2元，就可以上公交车;没钱,撵走；如果空座位的数量大于0，就可以坐下;
"""a=int(input("请输入公交卡余额:"))
if a > 2 :
    print("可以上公交车")
    b = int(input("请输入空座位数:"))
    if b > 0 :
        print("可以坐下")
else:
    print("撵走")"""

"""7.成绩等级:
	90分以上:  等级为A

	80-90: 等级为B
		
	60-80: 等级C
	 
	0-50: 等级为D"""
"""a=int(input("请输入成绩:"))
if a >= 0 and a <= 50 :
    print("%s成绩等级为D"%(a))
else:
    if a >= 60 and a <= 80 :
        print("%s成绩等级为C"%(a))
    else:
        if a >= 80 and a <= 90:
            print("%s成绩等级为B"%(a))
        else:
            if a > 90:
                print("%s成绩等级为A"%(a))
            else:
                print("%s成绩没有等级"%(a))"""

"""8.场景应用: 上火车 (用户输入表示是否有票,是否有刀具)
	是否有票,有票打印可以进站;
	进站查看是否带有刀具,有刀具,没收上车,没有刀具,直接上车
	没票打印不可以进站"""
"""a=input("请输入是否有票:")
if a == "是" :
    print("可以进站")
    b = input("请输入是否有刀具:")
    if b == "是" :
        print("没收上车")
    else:
        print("直接上车")
else:
    print("不可以进站")"""

"""9.女友的节日: 
	定义holiday_name字符串变量记录节日名称
	如果是 情人节 应该 买玫瑰／看电影
	如果是 平安夜 应该 买苹果／吃大餐
	如果是 生日 应该 买蛋糕
	其他的时候,每天都是节日"""
# holiday_name=input("节日名称为:")
# a=""" 应该 买玫瑰／看电影"""
# b=""" 应该 买苹果／吃大餐"""
# c=""" 应该 买蛋糕"""
# d="""其他的时候,每天都是节日"""
# if holiday_name == "情人节" :
#     print("%s%s"%(holiday_name,a))
# else:
#     if holiday_name == "平安夜":
#         print("%s%s"%(holiday_name,b))
#     else:
#         if holiday_name == "生日":
#             print("%s%s"%(holiday_name,c))
#         else:
#             print("%s"%(d))

"""10.英雄联盟(LOL)李青技能:
	q,Q:天音波 
	w,W:金钟罩/铁布衫
	e,E:天雷破/摧筋断骨
	r,R:猛龙摆尾"""
# j=input("请输入按下的键盘按键:")
# a="""Q:天音波 """
# b="""W:金钟罩/铁布衫"""
# c="""E:天雷破/摧筋断骨"""
# d="""R:猛龙摆尾"""
# if j == "q" :
#     print(a)
# else:
#     if j == "w":
#         print(b)
#     else:
#         if j == "e":
#             print(c)
#         else:
#             if j == "r":
#                 print(d)

# 11.用户决定是否发工资,工资数是多少,信用卡欠款;有剩余的时候,显示剩余金额(图1)
# a=input("今天发工资?")
# h="""又可以 Happy 了"""
# o="""噢, no"""
# if a == "Yes" :
#     print("先还信用卡的钱")
#     b=input("还有剩余吗?")
#     if b == "Yes" :
#         print(h)
#     else:
#         print(o)
# else:
#     print("盼工资")


# 12.让用户输入三个任意的整数, 比较三个数的大小, 输出最大的数
"""a=int(input("请输入第1个整数:"))
b=int(input("请输入第2个整数:"))
c=int(input("请输入第3个整数:"))
t=0
if a > b :
    if a > c :
        t=a
        print("%s是最大的数"%(t))
    else:
        t=c
        print("%s是最大的数"%(t))
else:
    if b > c :
        t=b
        print("%s是最大的数"%(t))
    else:
        t=c
        print("%s是最大的数"%(t))"""


