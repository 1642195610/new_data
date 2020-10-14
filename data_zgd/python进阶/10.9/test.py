# # 入环点
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# def huan(head):
#     fast = slow = head
#     while fast and fast.next:
#         fast, slow = fast.next.next, slow.next
#         if fast == slow:
#             slow = head
#             while fast != slow:
#                 fast, slow = fast.next, slow.next
#             return slow
#
#
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# # node6.next = node2
# print(huan(node1))
#

class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0:
            raise IndexError("数组越界")
        if index >= len(self.array) or self.size >= len(self.array):
            self.add_capacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("数组越界")
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def add_capacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def out_put(self):
        print(self.array)


array = Array(4)
array.insert(0, 0)
array.insert(1, 1)
array.insert(2, 2)
array.insert(0, 100)
array.insert(4, 400)
array.insert(2, 300)
array.out_put()
array.remove(0)
array.out_put()
array.remove(4)
array.out_put()
array.remove(1)
array.out_put()
