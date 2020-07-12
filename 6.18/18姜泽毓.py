"""
:作者:  姜泽毓
:Create:  2020/6/19 10:17
:CSDN:  http://blog.csdn.net/qq_43722162
Copyright (c) 2020, 姜泽毓 Group All Rights Reserved.
"""


class Sz:  # 创建类
    def __init__(self, shuliang):  # 定义数组函数
        self.sz = [None] * shuliang  # 数组容量
        self.geshu = 0  # 有效数据

    def charu(self, weizhi, zhi):  # 定义插入函数
        """

        :param weizhi:
        :type weizhi:
        :param zhi:
        :type zhi:
        :return:
        :rtype:
        """
        if weizhi < 0 or weizhi > self.geshu:  # 如果要插入的位置是负数或者大于有效数据的个数,就数组越界啦
            raise Exception('数组越界')
        if self.geshu >= len(self.sz):  # 如果要插入的数量大于原数组就要扩展数组容量
            self.add()
        for i in range(self.geshu - 1, weizhi - 1, -1):
            self.sz[i + 1] = self.sz[i]  # 原数组数据都往后从要插入的位置后移
        self.sz[weizhi] = zhi
        self.geshu += 1

    def add(self):  # 定义扩展数组函数
        new = [None] * len(self.sz) * 2
        for i in range(self.geshu):
            new[i] = self.sz[i]
        self.sz = new

    def dell(self, weizhi):
        if weizhi < 0 or weizhi > self.geshu:  # 如果要插入的位置是负数或者大于有效数据的个数,就数组越界啦
            raise Exception('数组越界')
        for i in range(weizhi, self.geshu):
            self.sz[i] = self.sz[i + 1]
        self.geshu -= 1

    def out(self):  # 定义格式化输出函数
        for i in range(self.geshu):
            print(self.sz[i], end='->')


if __name__ == '__main__':
    s = Sz(4)
    s.charu(0, 0)
    s.charu(1, 1)
    s.charu(2, 2)
    s.charu(3, 3)
    s.charu(4, 4)
    s.out()
    print('\n')
    s.dell(1)
    s.out()
