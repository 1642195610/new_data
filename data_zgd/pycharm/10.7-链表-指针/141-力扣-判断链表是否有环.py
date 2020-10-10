# 141.环形链表-力扣
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkList:  # 第一种
#     def huan(self, head):
#         if head is None or head.next is None:
#             return False
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False

# class LinkList: #第二种
#     def huan(self, head):
#         fast = slow = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False


class LinkList:  # 假第三种:解构
    def huan(self, head: Node):
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1
ll = LinkList()
print(f"链表是否有环: {ll.huan(n1)}")
