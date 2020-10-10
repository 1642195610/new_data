class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        while l1:
            result.append(l1.val)
            l1 = l1.next
        while l2:
            result.append(l2.val)
            l2 = l2.next
        result.sort()
        cur = dummy = ListNode(0)
        for i in result:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return cur.next

    def print_t(self, zhead):
        curr = zhead
        s = ""
        while curr:
            s += f"{curr} -> "
            curr = curr.next
        return s + "END"


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = None
    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3
    n3.next = None
    s = Solution()
    print(f"第一个链表: {s.print_t(n1)}")
    print(f"第二个链表: {s.print_t(b1)}")
    r = s.mergeTwoLists(n1, b1)
    print(f"新链表头部为: {r}")
    print(f"新链表为: {s.print_t(r)}\n")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        elif l2 is None:
            cur.next = l1
        return dummy.next

    def print_t(self, zhead):
        curr = zhead
        s = ""
        while curr:
            s += f"{curr} -> "
            curr = curr.next
        return s + "END"


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = None
    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3
    n3.next = None
    s = Solution()
    print(f"第一个链表: {s.print_t(n1)}")
    print(f"第二个链表: {s.print_t(b1)}")
    r = s.mergeTwoLists(n1, b1)
    print(f"新链表头部为: {r}")
    print(f"新链表为: {s.print_t(r)}")
