# 1. 删除链表特定元素

# def Del(list, val):
#     m = 0
#     k = 0
#     while k < len(list):
#         if list[k] == val:
#             k += 1
#         else:
#             list[m] = list[k]
#             m += 1
#             k += 1
#     return



class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"({self.data})"


class ListLink:
    def __init__(self):
        self.head = None

    

