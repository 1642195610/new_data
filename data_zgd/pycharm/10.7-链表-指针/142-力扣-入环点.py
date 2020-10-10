# 142-力扣-入环点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


# class LinkList:
#     def huan(self, head):
#         fast = slow = head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 slow = head
#                 while slow != fast:
#                     slow = slow.next
#                     fast = fast.next
#                 return slow
#         return None

# class LinkList:
#     def huan(self, head):
#         fast = slow = head
#         while fast and fast.next:
#             fast, slow = fast.next.next, slow.next
#             if fast == slow:
#                 slow = head
#                 while fast != slow:
#                     fast, slow = fast.next, slow.next
#                 return slow
#         return None

class LinkList:
    def huan(self, head):
        fast = slow = head
        f = 0
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                f = 1
                break
        if f:
            slow = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n2
ll = LinkList()
print(f"入环点为: {ll.huan(n1)}")
