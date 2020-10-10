# from randomList import randomList
# from typing import *
#
# iList = randomList.randomList(10)
#
#
# def bubblesort(l: List[int]):
#     if len(l) <= 1:
#         return l
#     for i in range(1, len(l)):
#         for j in range(len(l) - 1):
#             if l[j] >= l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#         print("第{}轮排序结果".format(i), end=" ")
#         print(l)
#     return l
#
#
# if __name__ == '__main__':
#     print("原始数据: ", iList)
#     print(bubblesort(iList))
#

from typing import List
from randomList import randomList
from typing import *

iList = randomList.randomList(10)


def mp(l: List[int]):
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):
        for j in range(len(l) - 1):
            if l[j] >= l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        print("第%s轮排序结果: " % i, end=" ")
        print(l)
    return l


if __name__ == '__main__':
    print("原始数据: ", iList)
    print("冒泡最终的结果: ", mp(iList))
    print()


iList = randomList.randomList(10)


def xz(l: List[int]):
    if len(l) <= 1:
        return l
    for i in range(len(l) - 1):
        max = i
        for j in range(i + 1, len(l)):
            if l[j] < l[max]:
                max = j
        l[i], l[max] = l[max], l[i]
        print("第%s轮排序结果: " % i, end=" ")
        print(l)
    return l


if __name__ == '__main__':
    print("原始数据: ", iList)
    print("选择最终的结果: ", xz(iList))
