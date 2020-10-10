"""
Author:     Mr.Jiang
Github:     https://github.com/1642195610
CSDN  :     https://blog.csdn.net/qq_43722162
"""

from typing import List


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        # return "Node(%s)" % self.data # 第一种
        # return "Node({})".format(self.data)  # 第二种
        return f"Node({self.data})"  # 第三种


n = Node(3)


# print(n)


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):  # 头部插入
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):  # 尾部插入
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def insert(self, i, data):  # 中间插入
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1  # 记录走了多少步
            pre = temp
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = temp

    def linklist(self, object: List):  # 列表插入
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            temp.next = Node(i)
            temp = temp.next

    def delete_head(self):  # 删除头部
        if self.head is None:
            return Exception is print("链表为空!!!无需删除!!!")
        else:
            temp = self.head
            self.head = self.head.next

    def delete_tail(self):  # 删除尾部
        if self.head is None:
            return Exception is print("链表为空!!!无需删除!!!")
        else:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def __repr__(self):
        curr = self.head
        str = ""
        while curr:
            str += f"{curr} --> "  # 第一种
            # str += "{} --> ".format(curr)  # 第二种
            # str += "%s --> " % curr  # 第三种
            curr = curr.next
        return str + "END"


ll = LinkList()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.append(4)
ll.insert(3, 300)
print("一个一个插入的链表: %s" % ll)
ll.linklist(list(range(1, 7)))
print("列表的每一个元素为链表的每一个元素: %s" % ll)
print()
print("原链表为: %s" % ll)
ll.delete_head()
print("删除头部: {}".format(ll))
print()
print(f"原链表为: {ll}")
ll.delete_tail()
print(f"删除尾部: {ll}")
