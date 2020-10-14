"""
Author:     Mr.Jiang
Github:     https://github.com/1642195610
CSDN  :     https://blog.csdn.net/qq_43722162
"""

# from typing import List
#
#
# class Node:
#     def __init__(self, data, next=None):
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
#     def __repr__(self):
#         curr = self.head
#         str = ""
#         while curr:
#             str += f"{curr} --> "
#             curr = curr.next
#         return str + "END"
#
#     def insert_head(self, data):  # 头部插入
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         else:
#             self.head = new_node
#         self.head = new_node
#
#     def append(self, data):  # 尾部插入
#         new_node = Node(data)
#         if self.head is None:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#
#     def insert(self, i, data):  # 中间插入
#         if self.head is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             j = 1
#             pre = temp
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             new_node = Node(data)
#             pre.next = new_node
#             new_node.next = temp
#
#     def linklist(self, obj: List):  # 列表插入
#         self.head = Node(obj[0])
#         temp = self.head
#         for i in obj[1:]:
#             temp.next = Node(i)
#             temp = temp.next
#
#     def delete_head(self):  # 删除头部
#         if self.head is None:
#             return Exception is print("链表为空!!!无需删除!!!")
#         else:
#             self.head = self.head.next
#
#     def delete_tail(self): # 删除尾部
#         if self.head is None:
#             return Exception is print("链表为空!!!无需删除!!!")
#         else:
#             temp = self.head
#             while temp.next.next:
#                 temp = temp.next
#             temp.next = None
#
#
# ll = LinkList()
# ll.insert_head(1)
# ll.insert_head(2)
# ll.insert_head(3)
# ll.append(4)
# ll.insert(3, 200)
# print(ll)
# ll.linklist(list(range(1, 7)))
# print(ll)
# print()
# print(f"原链表为: {ll}")
# ll.delete_head()
# print("删除头部: {}".format(ll))
# print()
# print(f"原链表为: {ll}")
# ll.delete_tail()
# print("删除尾部: {}".format(ll))


# from typing import List
#
#
# class Node:
#     def __init__(self, data, next = None):
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
#     def __repr__(self):
#         curr = self.head
#         str = ""
#         while curr:
#             str += f"{curr} --> "
#             curr = curr.next
#         return str + "END"
#
#     def insert_head(self,data): # 头部插入
#         new_node = Node(data)
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node.next = self.head
#         self.head = new_node
#
#     def insert_append(self,data): # 尾部插入
#         new_node = Node(data)
#         if self.head is None:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#
#     def insert(self, i, data): # 中间插入
#         new_node = Node(data)
#         if self.head is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             j = 1
#             pre = temp
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             pre.next = new_node
#             new_node.next = temp
#
#     def linklist(self, obj: List): # 链表插入
#         self.head = Node(obj[0])
#         temp = self.head
#         for i in obj[1:]:
#             temp.next = Node(i)
#             temp = temp.next
#
#     def delete_head(self): # 删除头部
#         if self.head is None:
#             return Exception is print("链表为空,无需删除!!!")
#         else:
#             self.head = self.head.next
#
#     def delete_tail(self): # 删除尾部
#         if self.head is None:
#             return Exception is print("链表为空,无需删除!!!")
#         else:
#             curr = self.head
#             while curr.next.next:
#                 curr = curr.next
#             curr.next = None
#
#
# ll = LinkList()
# ll.insert_head(1)
# ll.insert_head(2)
# ll.insert_head(3)
# ll.insert_append(4)
# ll.insert(3,300)
# print(ll)
# ll.linklist(list(range(1,7)))
# print(ll)
# print()
# print(f"原链表为: {ll}")
# ll.delete_head()
# print(f"删除头部: {ll}")
# print()
# print("原链表为: %s"%ll)
# ll.delete_tail()
# print("删除尾部: {}".format(ll))


from typing import List


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        curr = self.head
        str1 = ""
        while curr:
            str1 += f"{curr} --> "
            curr = curr.next
        return str1 + "END"

    def insert_head(self, data):  # 头部插入
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def insert_append(self, data):  # 尾部插入
        new_node = Node(data)
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, i, data):  # 中间插入
        new_node = Node(data)
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            pre = temp
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            pre.next = new_node
            new_node.next = temp

    def linklist(self, obj: List):  # 链表插入
        self.head = Node(obj[0])
        temp = self.head
        for i in obj[1:]:
            temp.next = Node(i)
            temp = temp.next

    def delete_head(self):  # 删除头部
        if self.head is None:
            return Exception is print("链表为空,无需删除")
        else:
            self.head = self.head.next

    def delete_tail(self):  # 删除尾部
        if self.head is None:
            return Exception is print("链表为空,无需删除")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None


ll = LinkList()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_append(4)
ll.insert(3, 300)
print(ll)
ll.linklist(list(range(1, 7)))
print(ll)
print()
print(f"原链表为: {ll}")
ll.delete_head()
print(f"删除头部: {ll}")
print()
print(f"原链表为: {ll}")
ll.delete_tail()
print(f"删除尾部: {ll}")
