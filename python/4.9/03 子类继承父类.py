# class Person:
#     def eat(self):
#         print("%s在吃饭"%(self.name))
#     def run(self):
#         print("%s在跑步" % (self.name))
#     def __init__(self,a,b,c,d):
#         self.id = a
#         self.name = b
#         self.sg = c
#         self.tz = d
# class Student (Person):
#     def eat(self):
#         print("%s在食堂吃饭"%(self.name))
# class Worker (Person):
#     def run(self):
#         print("%s在跑步机上跑步" % (self.name))
# s = Student(111,"张三",175,70)
# s.eat()
# s.run()
# w = Worker(222,"李四",180,90)
# w.eat()
# w.run()

# class Person:
#     def eat(self):
#         print("%s在吃饭"%(self.name))
#     def run(self):
#         print("%s在跑步" % (self.name))
#     def __init__(self,a,b,c,d):
#         self.id = a
#         self.name = b
#         self.sg = c
#         self.tz = d
# class Student (Person):
#     def __init__(self,a,b,c,d,e):
#         super().__init__(a,b,c,d)
#         self.scroe = e
#     def eat(self):
#         print("%s在食堂吃饭"%(self.name))
#     def cj(self):
#         print("成绩为:%s" % (self.scroe))
# class Worker (Person):
#     def __init__(self,a,b,c,d,e):
#         super().__init__(a,b,c,d)
#         self.gongz = e
#     def run(self):
#         print("%s在跑步机上跑步" % (self.name))
#     def gz(self):
#         print("工资为:%s"%(self.gongz))
# s = Student(111,"张三",175,70,100)
# s.eat()
# s.run()
# s.cj()
# w = Worker(222,"李四",180,90,10000)
# w.eat()
# w.run()
# w.gz()

