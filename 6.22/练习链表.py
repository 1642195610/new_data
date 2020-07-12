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
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current
#
#     def insert(self, index, element):
#         new_node = Node(element)
#         if index < 0 or index > self.size:
#             raise Exception("索引越界!!!")
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
#     def remove(self,index):
#         remove_node = None
#         if index < 0 or index > self.size:
#             raise Exception("索引越界!!!")
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
#
#     def __repr__(self):
#         current = self.head
#         resualt = ""
#         while current:
#             resualt += f"{current} -->"
#             current = current.next
#         return resualt + "END"
#
#
# if __name__ == "__main__":
#     j = LinkList()
#     j.insert(0, 1)
#     j.insert(1, 2)
#     j.insert(2, 3)
#     print("链表为: %s" % (j))
#     j.remove(1)
#     print("删除后链表为: %s"%(j))


# from typing import List
#
#
# class Node:
#     def __init__(self,data):
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
#     def __repr__(self):
#         current = self.head
#         resualt = ""
#         while current:
#             resualt += f"{current} --> "
#             current = current.next
#         return resualt + "END"
#
#     def get(self,index):
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current
#
#     def insert(self,index,data):
#         new_node = Node(data)
#         if index < 0 or index > self.size:
#             raise Exception("索引越界!!!")
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
#     def remove(self,index):
#         remove_node = Node
#         if index < 0 or index > self.size:
#             raise Exception("索引越界!!!")
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
#
# if __name__ == "__main__":
#     j = LinkList()
#     j.insert(0,100)
#     j.insert(1,200)
#     j.insert(2,300)
#     print("链表为: %s"%(j))
#     j.remove(1)
#     print("删除后链表为: %s"%(j))


from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        current = self.head
        resualt = ""
        while current:
            resualt += f"{current} --> "
            current = current.next
        return resualt + "END"

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def insert(self, index, element):
        new_node = Node(element)
        if index < 0 or index > self.size:
            raise Exception("索引越界!!!")
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def remove(self, index):
        remove_node = None
        if index < 0 or index > self.size:
            raise Exception("索引越界!!!")
        elif index == 0:
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1


if __name__ == "__main__":
    j = LinkList()
    j.insert(0, 100)
    j.insert(1, 200)
    j.insert(2, 300)
    j.insert(3, 400)
    j.insert(4, 500)
    j.insert(5, 600)
    print("链表为: %s" % (j))
    j.remove(3)
    print("删除后链表为: %s" % (j))
