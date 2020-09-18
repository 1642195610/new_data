from randomList import randomList
from typing import List


iList = randomList.randomList(10)


def insertSort(iList: List) -> List:
    if len(iList) <= 1:
        return iList
    for right in range(1, len(iList)):
        target = iList[right]
        for left in range(0, right):
            if iList[left] > target:
                iList[left + 1:right + 1] = iList[left:right]
                iList[left] = target
                break
        print("第{}轮排序结果: ".format(right), end=" ")
        print(iList)
    return iList


if __name__ == '__main__':
    print("原始数据: ", iList)
    print("插入排序最终结果: ",insertSort(iList))
