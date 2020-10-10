"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


from typing import List
from pprint import pformat


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"({self.val}) --> "


class Solution:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curr = self.head
        res = " "
        while curr:
            res += f"({self.head}) --> "
            curr = curr.next
        return res + "END"

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            slow = pre.next
            fast = pre.next.next
            pre.next = fast
            slow.next = fast.next
            fast.next = slow
            pre = pre.next.next
        return dummy.next


if __name__ == '__main__':
    j1 = ListNode(1)
    j2 = ListNode(2)
    j3 = ListNode(3)
    j4 = ListNode(4)
    j1.next = j2
    j2.next = j3
    j3.next = j4
    j = Solution()
    j.swapPairs(j1)
    print(j)
''