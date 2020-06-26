# from typing import List
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def get(self, index):
#         curr = self.head
#         for _ in range(index):
#             curr = curr.next
#         return curr
#
#     def insert(self, index, element):
#         new_node = Node(element)
#         if index < 0 or index > self.size:
#             raise Exception("索引越界")
#         elif self.size == 0:
#             self.head = new_node
#             self.tail = new_node
#         elif index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         elif index == self.size:
#             self.tail.next = new_node
#             self.tail = new_node
#         else:
#             prev = self.get(index - 1)
#             new_node.next = prev.next
#             prev.next = new_node
#         self.size += 1
#
#     def __repr__(self):
#         curr = self.head
#         string = ""
#         while curr:
#             string += f"{curr} -->"
#             curr = curr.next
#         return string + "END"
#
#     def remove(self, index):
#         if index < 0 or index > self.size:
#             raise Exception("索引越界")
#         elif index == 0:
#             remove_node = self.head
#             self.head = self.head.next
#         elif index == self.size:
#             prev = self.get(index - 1)
#             remove_node = prev.next
#             prev.next = None
#             self.tail = prev
#         else:
#             prev = self.get(index - 1)
#             remove_node = prev.next
#             prev.next = prev.next.next
#         self.size -= 1
#
#     def reverse(self):
#         prev = None
#         curr = self.head
#         while curr:
#             temp = curr.next
#             if prev is None:
#                 curr.next = prev
#             else:
#                 curr.next = prev
#             prev = curr
#             curr = temp
#         self.head = prev
#
#
# if __name__ == '__main__':
#     j = LinkList()
#     j.insert(0, 100)
#     j.insert(1, 200)
#     j.insert(2, 300)
#     print("链表为: %s" % (j))
#     print("get获取为: {}".format(j.get(1)))
#     j.remove(1)
#     print("删除元素后链表为: %s" % (j))
#     j.reverse()
#     print("反转链表为: %s" % (j))



