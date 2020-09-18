# class Person:
#     def chi(self,a):
#         print("吃饭,今天吃%s"%(a))
#     def wan(self,a):
#         print("玩,今天玩%s"%(a))
# c = Person()
# c.chi("糖醋里脊")
# c.wan("王者荣耀文件夹")

# class Student:
#     def xm(self,a):
#         print("姓名:%s"%(a),end="\t")
#     def xh(self,a):
#         print("学号:%s" % (a),end="\t")
#     def sg(self,a):
#         print("身高:%s" % (a),end="\t")
# s = Student()
# s.xm("张三")
# s.xh(16201495)
# s.sg(175)
# print()
# s.xm("李四")
# s.xh(16201499)
# s.sg(185)

# class Niao:
#     def zl(self,a):
#         print("种类:%s"%(a),end="\t")
#         return a
#     def tz(self,a):
#         print("体重:%s"%(a),end="\t")
#         return a
#     def cb(self,a):
#         print("翅膀:%s"%(a),end="\t")
#         return a
# s = Niao()
# a = s.zl("小鸟")
# b = s.tz(12)
# c = s.cb(45)
# print()
# print("%s在用%s个翅膀在飞,体重是%s"%(a,c,b))

#在类中
# class Student:
#     def __init__(self,a,b,c):
#         self.name = a
#         self.xuehao = b
#         self.shengao = c
#     def p(self):
#         print("姓名:%s 学号:%s 身高:%s"%(self.name,self.xuehao,self.shengao))
# s = Student("张三",111,175)
# s1 = Student("李四",222,185)
# s.p()
# s1.p()

# class Niao:
#     def __init__(self,a,b,c):
#         self.zl = a
#         self.cb = b
#         self.tz = c
#     def f(self):
#         print("%s在用%s个翅膀在飞,体重是%s"%(self.zl,self.cb,self.tz))
# s = Niao("小鸟",45,30)
# s.f()




