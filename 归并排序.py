from randomList import randomList
from typing import List


iList = randomList.randomList(10)


def mergeSort(iList: List):
    if len(iList) <= 1:
        return iList
    middle = len(iList) // 2
    left, right = iList[:middle], iList[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left: List, right: List):
    mList = []
    while left and right:
        if left[0] >= right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))
    while left:
        mList.append(left.pop(0))
    while right:
        mList.append(right.pop(0))
    return mList


if __name__ == '__main__':
    print("原始数据: ", iList)
    print("归并排序: ", mergeSort(iList))
