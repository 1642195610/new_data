# class JieDian:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):  # 重写方法
#         # return '%s'%(self.data)
#         # return "{}".format(self.data)
#         return f"JieDian({self.data})"
#
#
# class LianBiao:
#     def __init__(self):
#         self.head = None
#
#     def charu(self, data):
#         new = JieDian(data)
#         if self.head:
#             new.next = self.head
#         self.head = new
#
#     def __repr__(self):
#         current = self.head
#         string_repr = ""
#         while current:
#             string_repr += f"{current} --> "
#             current = current.next
#         return string_repr + "END"
#
#
# if __name__ == '__main__':
#     j = LianBiao()
#     j.charu(100)
#     j.charu(199)
#     j.charu(198)
#     print(j)


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
#
#     def insert_head(self, data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#
#     def print_list(self):  # 只打印链表里面的值
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
#
#     def __repr__(self):
#         current = self.head
#         result = ""
#         while current:
#             result += f"{current} -->"
#             current = current.next
#         return result + "END"
#
#     def append(self, data):
#         if self.head is None:
#             self.insert_head(data)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = Node(data)
#
#     def insert(self, i, data):
#         if self.head is None or i == 1:
#             self.insert_head(data)
#         else:
#             curr = self.head
#             prev = self.head
#             j = 1
#             while j < i:
#                 prev = curr
#                 curr = curr.next
#                 j += 1
#             new_node = Node(data)
#             prev.next = new_node
#             new_node.next = curr
#
#     def linklist(self, obj: List):
#         new_node = Node(obj[0])
#         self.head = new_node
#         curr = self.head
#         for i in obj[1:]:
#             curr.next = Node(i)
#             curr = curr.next
#
#     def delete_head(self):
#         if self.head is None:
#             print('空链表')
#         else:
#             self.head = self.head.next
#
#     def pop(self):
#         curr = self.head
#         if self.head is None:
#             print('空链表')
#         else:
#             while curr.next.next:
#                 curr = curr.next
#             temp = curr.next.data
#             curr.next = None
#         return temp
#
#     def delete_tail(self):
#         curr = self.head
#         prev = self.head
#         while curr.next :
#             prev = curr
#             curr = curr.next
#         else:
#             temp = curr
#             prev.next = None
#         return temp
#
#
# if __name__ == '__main__':
#     j = LinkList()
#     print("插入头部链表:",end=" ")
#     j.insert_head(9)
#     j.insert_head(6)
#     j.insert_head(3)
#     print(j)
#     print("插入尾部链表:",end=" ")
#     j.append(19)
#     j.append(16)
#     j.append(13)
#     print(j)
#     print("插入中间链表:",end=" ")
#     j.insert(3,33)
#     print(j)
#     print("插入多链表:",end=" ")
#     j.linklist([99,88,77])
#     print(j)
#     print("删除头部链表:",end=" ")
#     j.delete_head()
#     print(j)
#     print("删除元素为:  %s" % (j.pop()))
#     print("删除尾部链表:  %s" % (j))


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
#
#     def insert_head(self, data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
#
#     def __repr__(self):
#         current = self.head
#         resualt = ""
#         while current:
#             resualt += f"{current} -->"
#             current = current.next
#         return resualt + "END"
#
#     def append(self, data):
#         if self.head is None:
#             self.insert_head(data)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = Node(data)
#
#     def insert(self, i, data):
#         if self.head is None or i == 0:
#             self.insert_head(data)
#         else:
#             current = self.head
#             prev = self.head
#             j = 0
#             while j < i:
#                 prev = current
#                 current = current.next
#                 j += 1
#             new_node = Node(data)
#             prev.next = new_node
#             new_node.next = current
#
#     def linklist(self, obj: List):
#         new_node = Node(obj[0])
#         self.head = new_node
#         current = self.head
#         for i in obj[1:]:
#             current.next = Node(i)
#             current = current.next
#
#     def delete_head(self):
#         if self.head is None:
#             print("这是一个空链表")
#         else:
#             self.head = self.head.next
#
#     def pop(self):
#         current = self.head
#         if self.head is None:
#             print("这是一个空链表")
#         else:
#             while current.next.next:
#                 current = current.next
#             temp = current.next
#             current.next = None
#         return temp
#
#     def delete_tail(self):
#         current = self.head
#         prev = self.head
#         while current.next:
#             prev = current
#             current = current.next
#         else:
#             temp = current
#             prev.next = None
#         return temp
#
#
# if __name__ == "__main__":
#     j = LinkList()
#     print("插入头部链表:",end=" ")
#     j.insert_head(9)
#     j.insert_head(6)
#     j.insert_head(3)
#     print(j)
#     print("插入尾部链表:",end=" ")
#     j.append(19)
#     j.append(16)
#     j.append(13)
#     print(j)
#     print("插入中间链表:",end=" ")
#     j.insert(3,33)
#     print(j)
#     print("插入多链表:",end=" ")
#     j.linklist([99,88,77])
#     print(j)
#     print("删除头部链表:",end=" ")
#     j.delete_head()
#     print(j)
#     print("删除元素为:  %s" % (j.pop()))
#     print("删除尾部链表:  %s" % (j))
