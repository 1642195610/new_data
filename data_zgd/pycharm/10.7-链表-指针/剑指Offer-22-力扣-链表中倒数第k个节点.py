class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def find(self, head, k):
        curr = head
        while head.next:
            if k > 1:
                k -= 1
            else:
                curr = curr.next
            head = head.next
        return curr


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    ll = LinkList()
    k = 2
    print(f"链表倒数第{k}个结点为: {ll.find(n1, k)}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def find(self, head, k):
        slow = fast = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    ll = LinkList()
    k = 2
    print(f"链表倒数第{k}个结点为: {ll.find(n1, k)}")
