class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"({self.data})"

def merge(l1,l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 or l2:
        if l2.data < l1.data:
            cur.next = ListNode(l2.data)
            l2 = l2.next
        else:
            cur.next = ListNode(l1.data)
            l1 = l1.next
        cur = cur.next
        if l1 is None:
            cur.next = l2
            break
        if l2 is None:
            cur.next = l1
            break
    return dummy.next
def listres(head: ListNode):
    curr = head
    res = ""
    while curr:
        res += f"{curr} --> "
        curr = curr.next
    return res + "END"


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(5)
    node3 = ListNode(6)
    node4 = ListNode(7)
    node5 = ListNode(2)
    node6 = ListNode(3)
    node7 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    node5.next = node6
    node6.next = node7
    node7.next = None
    print("第1个链表: ",listres(node1))
    print("第2个链表: ",listres(node5))
    print("合并后链表: ",listres(merge(node1,node5)))



