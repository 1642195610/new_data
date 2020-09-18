# 1.Employee 类
# 	- 员工数 初始值为0, 每当新声明一个实例时,员工数加一
# 	- 员工: 姓名, 工资
# 	- 声明方法 displayCount: 打印出当前的总员工数 (类方法)
# 	- displaySalary : 打印每一个员工自己的名字和薪水.
# class Employee:
#     s = 0
#     def __init__(self,a,b):
#         self.name = a
#         self.gz = b
#         Employee.s += 1
#     def displaySalary(self):
#         print("姓名:%s  薪水:%s"%(self.name,self.gz))
#     @classmethod
#     def displayCount(cls):
#         print("总员工数:%s"%(cls.s))
# e1 = Employee("张三",10000)
# e2 = Employee("李四",20000)
# e3 = Employee("王五",30000)
# e1.displaySalary()
# e2.displaySalary()
# e3.displaySalary()
# Employee.displayCount()

# 2.设计一个人的类,有名字,体重;能吃,能跑;
# 	a.每次跑步会减肥0.5公斤
# 	b.每次吃东西体重会增加1公斤
# 	c.有个get_msg()方法,打印出名字,体重:
# 		我的名字叫: xxx 体重是:
# class Person:
#     def __init__(self,a,b):
#         self.name = a
#         self.tz = b
#     def run(self):
#         self.tz -= 0.5
#     def eat(self):
#         self.tz += 1
#     def get_msg(self):
#         print("我的名字叫:%s  体重是:%s"%(self.name,self.tz))
# p = Person("张三",70)
# p.run()
# p.eat()
# p.get_msg()

# 3.定义一个圆类,有半径属性,其中有计算周长和面积的方法
# class Yuan:
#     def __init__(self,a):
#         self.bj = a
#     def zc(self):
#         c = 2 * 3.14 * self.bj
#         print("周长:%s"%(c))
#     def mj(self):
#         s =  3.14 * (self.bj ** 2)
#         print("面积:%s"%(s))
# y1 = Yuan(1)
# y2 = Yuan(2)
# y1.zc()
# y1.mj()
# y2.zc()
# y2.mj()

# 4.补充代码实现:
# 	user_list = []
# 	while True:
# 		user_name = input('输入用户名: ')
# 		sex = input('输入性别: ')
# 		age = input('输入年龄: ')
# 		email = input('输入邮箱: ')
# 	a.把每个用户用对象表示
# 	b.当列表中添加3个对象以后,打印出3个对象的信息:
# 		我叫xxx,性别xx,今年xx岁了,我的邮箱是xxxx
# class Yh:
#     def __init__(self,a,b,c,d):
#         self.name = a
#         self.sex = b
#         self.age = c
#         self.ad = d
#     def p(self):
#         return "我叫%s,性别%s,今年%s岁了,我的邮箱是%s"%(self.name,self.sex,self.age,self.ad)
# user_list = []
# while True:
#     if len(user_list) != 3:
#         user_name = input('输入用户名: ')
#         sex = input('输入性别: ')
#         age = input('输入年龄: ')
#         email = input('输入邮箱: ')
#         y = Yh(user_name, sex, age, email)
#         user_list.append(y.p())
#     else:
#         a = [print(x) for x in user_list]
#         break

# 5.模拟英雄联盟中的游戏人物的类:
# 	要求:
# 		a.创建Role(角色)类
# 		b.初始化方法中给对象封装 name,ad(攻击力),hp(血量)三个属性
# 		c.创建一个attack方法,此方法是实例化的两个对象,互相攻击的功能
# 			例:
# 				实例化一个Role对象,盖伦,ad为10,hp为100
# 				实例化另一个Role对象,亚索,ad为20,hp为80
# 		  attack方法要完成: '谁攻击谁,谁掉了多少血,还剩多少血的提示功能'
# class Role:
#     def __init__(self,a,b,c):
#         self.name = a
#         self.gjl = b
#         self.xl = c
#     def attack(self,another_name,another_xl):
#         self.a_name = another_name
#         self.a_xl = another_xl
#         print("%s攻击%s,%s掉了%s血,还剩%s血"%(self.name,self.a_name,self.a_name,self.gjl,self.a_xl - self.gjl))
# r1 = Role("盖伦",10,100)
# r2 = Role("亚索",20,80)
# r1.attack("亚索",80)
# r2.attack("盖伦",100)

# 6.模拟英雄联盟中的游戏人物的类:
# 	要求:
# 		a.创建Role(角色)类,有name,ad(攻击力),hp(血量)三个属性
# 		b.创建Arms(武器)类,有name,ad(攻击力),两个属性
# 		c.创建一个attack方法,此方法是实例化的两个对象,互相用武器攻击的功能
# 			例:
# 				实例化一个Role对象,名字为盖伦,ad为10,hp为100
# 				实例化另一Role个对象,名字为亚索,ad为20,hp为80
# 				实例化一个Arms对象,名字为无尽之刃,ad为40
#
# 		  attack方法要完成: '谁拿什么武器攻击谁,谁掉了多少血,还剩多少血的提示功能'
# class Role:
#     def __init__(self,a,b,c):
#         self.name = a
#         self.gjl = b
#         self.xl = c
#     def attack(self,another_name,another_xl,obj):
#         self.a_name = another_name
#         self.a_xl = another_xl
#         print("%s拿%s攻击%s,%s掉了%s血,还剩%s血"%(self.name,obj.name,self.a_name,self.a_name,self.gjl + obj.gjl,self.a_xl - self.gjl - a.gjl))
# class Arms:
#     def __init__(self,a,b):
#         self.name = a
#         self.gjl = b
# r1 = Role("盖伦",10,100)
# r2 = Role("亚索",20,80)
# a = Arms("无尽战刃",40)
# r1.attack("亚索",80,a)
# r2.attack("盖伦",100,a)


