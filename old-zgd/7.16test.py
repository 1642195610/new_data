# from randomList import randomList
# from typing import List
#
#
# iList = randomList.randomList(10)
#
#
# def insertSort(iList: List) -> List:
#     if len(iList) <= 1:
#         return iList
#     for right in range(1, len(iList)):
#         target = iList[right]
#         for left in range(0, right):
#             if iList[left] > target:
#                 iList[left + 1:right + 1] = iList[left:right]
#                 iList[left] = target
#                 break
#         print("第{}轮排序结果: ".format(right), end=" ")
#         print(iList)
#     return iList
#
#
#
#
# if __name__ == '__main__':
#     print("原始数据: ", iList)
#     print("插入排序最终结果: ",insertSort(iList))


# from randomList import randomList
# from typing import List
#
#
# iList = randomList.randomList(10)
#
#
# def cr(l: List):
#     if len(l) <= 1:
#         return l
#     for right in range(1,len(l)):
#         f = l[right]
#         for left in range(0,right):
#             if l[left] > f:
#                 l[left+1:right+1] = l[left:right]
#                 l[left] = f
#                 break
#         print("第%s轮排序结果: "%right,end=" ")
#         print(l)
#     return l
#
#
# if __name__ == '__main__':
#     print("原始数据: ",iList)
#     print("插入排序最终结果: ",cr(iList))


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"({self.data})"


def cr(head):
    dummy = ListNode(0)
    pre = dummy
    cur = head
    while cur:
        temp = cur.next
        while pre.next and pre.next.data < cur.data:
            pre = pre.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
        pre = dummy
    return dummy.next


def sc(head):
    cur = head
    res = ""
    while cur:
        res += f"{cur} --> "
        cur = cur.next
    return res + "END"


if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(4)
    node4 = ListNode(2)
    node5 = ListNode(6)
    node6 = ListNode(1)
    node7 = ListNode(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None
    print("插入排序前: ", sc(node1))
    print("插入排序后: ", sc(cr(node1)))


