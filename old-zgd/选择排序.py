from typing import List
from randomList import randomList


iList = randomList.randomList(10)


def selectionSort(iList: List[int]) -> List:
    if len(iList) <= 1:
        return iList
    for i in range(len(iList) - 1):
        minindex = i
        for j in range(i + 1, len(iList)):
            if iList[j] < iList[minindex]:
                minindex = j
        iList[i], iList[minindex] = iList[minindex], iList[i]
        print("第{}轮排序结果: ".format(i), end=" ")
        print(iList)
    return iList


if __name__ == '__main__':
    print("原始数据: ", iList)
    print(selectionSort(iList))



