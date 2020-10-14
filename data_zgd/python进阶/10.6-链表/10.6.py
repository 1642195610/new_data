"""
Author:     Mr.Jiang
Github:     https://github.com/1642195610
CSDN  :     https://blog.csdn.net/qq_43722162
"""


class Student():
    def __init__(self, name, sex, age):
        """

        :param name:姓名
        :type name: str
        :param sex: 性别
        :type sex: str
        :param age: 年龄
        :type age: int
        """
        self.name = name
        self.sex = sex
        self.age = age

    def learn(self):
        print("%s能自主学习" % self.name)

    def sleep(self):
        print("{}能自主休息".format(self.name))


l = Student("姜泽毓", "男", 24)
print(l.name)
print(l.sex)
print(l.age)
l.learn()
l.sleep()
