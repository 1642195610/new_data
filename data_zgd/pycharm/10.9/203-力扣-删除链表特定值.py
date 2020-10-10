"""
Author:     Mr.Jiang
Create:     2020/10/10 11:08
Github:     https://github.com/1642195610
CSDN  :     https://blog.csdn.net/qq_43722162
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def delete_val(self, head: ListNode, val: int):
        pre = dummy = ListNode(0)
        curr = dummy.next = head
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        return dummy.next

    def print_t(self, head):
        curr = head
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
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(f"原链表为: {s.print_t(node1)}")
    val = 2
    result = s.delete_val(node1, val)
    print(f"删除的指定值为: {val}")
    print(f"新头部为: {result}")
    print(f"新链表为: {s.print_t(result)}\n")


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def delete_val(self, head: ListNode, val: int):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

    def print_t(self, head):
        curr = head
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
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(f"原链表为: {s.print_t(node1)}")
    val = 2
    result = s.delete_val(node1, val)
    print(f"删除的指定值为: {val}")
    print(f"新头部为: {result}")
    print(f"新链表为: {s.print_t(result)}")
    result = s.delete_val(node1, 3)
