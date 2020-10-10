class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
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

    def print_t(self, zhead):
        curr = zhead
        s = ""
        while curr:
            s += f"{curr} -> "
            curr = curr.next
        return s + "END"


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    print(f"原链表为: {s.print_t(node1)}")
    result = s.swapPairs(node1)
    print(f"新头部为: {result}")
    result = s.print_t(result)
    print(f"新链表为: {result}")
