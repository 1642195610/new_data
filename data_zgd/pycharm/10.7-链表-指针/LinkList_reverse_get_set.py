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

    def reverse(self):  # 反转链表
        prev = None
        curr = self.head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        self.head = prev

    def __getitem__(self, index):  # 查找指定位置结点
        curr = self.head
        if curr is None:
            raise IndexError("链表为空,不能查找")
        for _ in range(1, index):
            if curr.next is None:
                raise IndexError("下标越界")
            curr = curr.next
        return curr

    def get(self, index):
        return self.__getitem__(index)

    def __setitem__(self, index, data):  # 更改指定位置结点
        curr = self.head
        if curr is None:
            raise IndexError("链表为空")
        for _ in range(1, index):
            if curr.next is None:
                raise IndexError("下标越界")
            curr = curr.next
        curr.data = data
        return curr

    def set(self, index, data):
        return self.__setitem__(index, data)


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
print()
print(f"原链表为: {ll}")
ll.reverse()
print(f"反转链表: {ll}")
print()
print(f"查找链表为  :{ll}")
index = 1
print(f"要查找的节点位置为: {index}, 对应的结点为: {ll.get(index)}")
print()
index = 2
print(f"更改前链表为: {ll}")
print(f"更改节点位置为: {index}, 对应节点为: {ll.get(index)} ,更改后节点为: {ll.set(index, 300)}")
print(f"更改后链表为: {ll}")
