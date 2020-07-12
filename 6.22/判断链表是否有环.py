# 判断链表是否有环

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# def pan(data):
#     curr = data
#     prev = data
#     while curr and curr.next is not None:
#         prev = prev.next
#         curr = curr.next.next
#         if prev == curr:
#             return True
#     return  False
#
#
# if __name__ == '__main__':
#     j1 = Node(1)
#     j2 = Node(2)
#     j3 = Node(3)
#     j1.next = j2
#     j2.next = j3
#     j3.next = j1
#     print(pan(j1))
