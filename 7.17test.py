class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return f'Node{self.data}'

def hebing(l1:ListNode,l2:ListNode):
    head=ListNode(0)
    cur=head
    while l1 is not None and l2 is not None:
        if l1.data<l2.data:
            cur.next=ListNode(l1.data)
            l1=l1.next
        else:
            cur.next=ListNode(l2.data)
            l2=l2.next
        cur=cur.next
    while l1:
        cur.next=ListNode(l1.data)
        l1=l1.next
        cur=cur.next
    while l2:
        cur.next=ListNode(l2.data)
        l2=l2.next
        cur=cur.next
    return head.next

def listres(head):
    curr=head
    res=''
    while curr:
        res=res+f'{curr}-->'
        curr=curr.next
    return res+'END'
if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(6)
    node4 = ListNode(1)
    node5 = ListNode(2)
    node6 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = None
    node4.next = node5
    node5.next = node6
    node6.next = None
    print(listres(node1))
    print(listres(node4))
    print(listres(hebing(node1,node4)))



