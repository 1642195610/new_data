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
#     def __repr__(self):
#         curr = self.head
#         s = ""
#         while curr:
#             s += f"{curr} --> "
#             curr = curr.next
#         return s + "END"
#
#     def get(self, index):
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
#
#     def insert(self, index, data):
#         new_node = Node(data)
#         if index < 0 or index > self.size:
#             raise IndexError("下标越界")
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
#     def remove(self, index):
#         temp = self.head
#         if index < 0 or index >= self.size:
#             raise IndexError("下标越界")
#         elif self.size == 0:
#             raise IndexError("链表为空")
#         elif index == 0:
#             self.head = temp.next
#             remove_node = temp
#             temp.next = None
#         elif index == self.size - 1:
#             prev = self.get(index - 1)
#             remove_node = prev.next
#             prev.next = None
#         else:
#             prev = self.get(index - 1)
#             remove_node = prev.next
#             prev.next = prev.next.next
#         self.size -= 1
#         return remove_node
#
#     def reverse(self):
#         prev = None
#         curr = self.head
#         while curr:
#             new_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = new_node
#         self.head = prev
#
#     def set(self, index, data):
#         if self.head is None:
#             raise IndexError("链表为空,无法更改")
#         else:
#             curr = self.get(index)
#             curr.data = data
#         return curr
#
#
# ll = LinkList()
# ll.insert(0, 0)
# ll.insert(1, 1)
# ll.insert(2, 2)
# ll.insert(0, -1)
# ll.insert(4, 30)
# print(ll)
# ll.remove(0)
# print(ll)
# ll.remove(3)
# print(ll)
# ll.remove(1)
# print(ll)
# ll.reverse()
# print(ll)
# ll.set(0, 100)
# print(ll)
#


# 判断有没有入环点,并输出入环点

from typing import Optional  # 类型注解和List基本一样


class Node:
    def __init__(self, data):
        self.val = data
        self.next = data

    def __repr__(self):
        return f"Node({self.val})"


def detect_cycle(head: Optional[Node] = None) -> Node:
    fast = slow = head
    f = False
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            f = True
            break
    if f:
        slow = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return slow


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node3
    result = detect_cycle(node1)
    print(result)
