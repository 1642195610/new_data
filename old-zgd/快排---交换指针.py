from typing import List
from randomList import randomList


iList = randomList.randomList(5)


def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def partition(iList,start,end):
    pivot = iList[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and iList[p] < pivot:
            p += 1
        while p <= q and iList[q] >= pivot:
            q -= 1
        if p < q:
            swap(iList,p,q)
    swap(iList,start,q)
    return q

def quickSort(iList,start,end):
    if start >= end:
        return
    mid = partition(iList,start,end)
    quickSort(iList,start,mid - 1)
    quickSort(iList,mid + 1,end)


if __name__ == '__main__':
    print("原列表: ",iList)
    quickSort(iList,0,len(iList) - 1)
    print("新列表: ",iList)
