class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Solution:
    def list(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            if l1.data <= l2.data:
                cur.next = ListNode(l1.data)
                l1 = l1.next
            elif l1.data > l2.data:
                cur.next = ListNode(l2.data)
                l2 = l2.next
            cur = cur.next
            if l1 is None:
                cur.next = l2
                break
            if l2 is None:
                cur.next = l1
                break
        return dummy.next

    def print_t(self, head):
        cur = head
        s = ""
        while cur:
            s += f"{cur} --> "
            cur = cur.next
        return s + "END"


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    snode1 = ListNode(1)
    snode2 = ListNode(3)
    snode3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = None
    snode1.next = snode2
    snode2.next = snode3
    snode3.next = None
    s = Solution()
    relult = s.list(node1, snode1)
    print(relult)
    r = s.print_t(relult)
    print(r)


class Solution1:
    def list(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.data <= l2.data:
                cur.next = ListNode(l1.data)
                l1 = l1.next
            elif l1.data > l2.data:
                cur.next = ListNode(l2.data)
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1
        return dummy.next

    def print_t(self, head):
        cur = head
        s = ""
        while cur:
            s += f"{cur} --> "
            cur = cur.next
        return s + "END"


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    snode1 = ListNode(1)
    snode2 = ListNode(3)
    snode3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = None
    snode1.next = snode2
    snode2.next = snode3
    snode3.next = None
    s = Solution1()
    relult = s.list(node1, snode1)
    print(relult)
    r = s.print_t(relult)
    print(r)


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("栈为空")
        else:
            temp = self.stack.pop()
            self.size -= 1
        return temp

