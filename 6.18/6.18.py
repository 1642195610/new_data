# print('我爱python就像爱自己生命一样哦!')
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def learn(self):
#         print("%s能自主学习!" % (self.name))
#
#
# s = Student('姜泽毓')
# print(s.name)
# s.learn()
#
#
# class Sz:
#     def __init__(self, szchangdu):
#         self.sz = [None] * szchangdu
#         self.geshu = 0
#
#     def charu(self, weizhi, zhi):
#         if weizhi < 0 or weizhi > self.geshu:
#             raise Exception('数组越界!!!')
#         if self.geshu >= len(self.sz):
#             self.add()
#         for i in range(self.geshu - 1, weizhi - 1, -1):
#             self.sz[i + 1] = self.sz[i]
#         self.sz[weizhi] = zhi
#         self.geshu += 1
#
#     def add(self):
#         new_sz = [None] * len(self.sz) * 2
#         for i in range(self.geshu):
#             new_sz[i] = self.sz[i]
#         self.sz = new_sz
#
#     def out(self):
#         for i in range(self.geshu):
#             print(self.sz[i], end='->')
#
#
# if __name__ == '__main__':
#     s = Sz(3)
#     s.charu(0, 10)
#     s.charu(1, 20)
#     s.charu(2, 30)
#     s.charu(3, 40)
#     s.out()
#
#
# class Sz:
#     def __init__(self, gs):
#         self.sz = [None] * gs
#         self.sl = 0
#
#     def cr(self, wz, z):
#         if wz < 0 or wz > self.sl:
#             raise Exception('数组越界!!!')
#         if self.sl >= len(self.sz):
#             self.add()
#         for i in range(self.sl - 1, wz - 1, -1):
#             self.sz[i + 1] = self.sz[i]
#         self.sz[wz] = z
#         self.sl += 1
#
#     def add(self):
#         new = [None] * len(self.sz) * 2
#         for i in range(self.sl):
#             new[i] = self.sz[i]
#         self.sz = new
#
#     def out(self):
#         for i in range(self.sl):
#             print(self.sz[i], end='->')
#
#
# if __name__ == '__main__':
#     s = Sz(3)
#     s.cr(0, 0)
#     s.cr(1, 1)
#     s.cr(2, 2)
#     s.cr(3, 3)
#     s.cr(4, 4)
#     s.out()


class Sz:
    def __init__(self, shuliang):
        self.sz = [None] * shuliang
        self.geshu = 0

    def charu(self, weizhi, zhi):
        if weizhi < 0 or weizhi > self.geshu:
            raise Exception('数组越界')
        if self.geshu >= len(self.sz):
            self.add()
        for i in range(self.geshu - 1, weizhi - 1, -1):
            self.sz[i + 1] = self.sz[i]
        self.sz[weizhi] = zhi
        self.geshu += 1

    def add(self):
        new = [None] * len(self.sz) * 2
        for i in range(self.geshu):
            new[i] = self.sz[i]
        self.sz = new

    def out(self):
        for i in range(self.geshu):
            print(self.sz[i], end='->')


if __name__ == '__main__':
    s = Sz(2)
    s.charu(0, 0)
    s.charu(1, 1)
    s.charu(2, 2)
    s.charu(3, 3)
    s.out()
