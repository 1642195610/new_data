from randomList import randomList
from typing import List

iList = randomList.randomList(5)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        resualt = ""
        while current:
            resualt += f"{current} --> "
            current = current.next
        return resualt + "END"

    def linklist(self, obj: List):
        new_node = Node(obj[0])
        self.head = new_node
        current = self.head
        for i in obj[1:]:
            current.next = Node(i)
            current = current.next

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
    return iList


if __name__ == "__main__":
    j = LinkList()
    j.linklist(iList)
    print("未排序的链表: %s" % (j))
    j.linklist(insertSort(iList))
    print("插入排序链表: %s" % (j))


