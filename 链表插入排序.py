class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"({self.data})"


def insertionSortList(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    pre = dummy
    cur = head
    while cur:
        temp = cur.next
        while pre.next and pre.next.data < cur.data:#找到待插入结点的位置
            pre = pre.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
        pre = dummy
    return dummy.next

def listres(head: ListNode):
    curr = head
    res = ""
    while curr:
        res += f"{curr} --> "
        curr = curr.next
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
    print(listres(node1))
    print(listres(insertionSortList(node1)))



















