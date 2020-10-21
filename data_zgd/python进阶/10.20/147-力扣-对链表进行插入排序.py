class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        cur = head
        while cur is not None:
            temp = cur.next
            while pre.next is not None and \
                    pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
            pre = dummy
        return dummy.next

    def print_p(self, node: ListNode):
        cur = node
        s = ""
        while cur:
            s += f"{cur} --> "
            cur = cur.next
        return s + "END"


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    print(f"未排序链表为: {s.print_p(node1)}")
    res = s.insertionSortList(node1)
    result = s.print_p(res)
    print(f"插入排序链表: {result}")
