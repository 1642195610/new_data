# from pprint import pformat
#
#
# class Node:
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#
#     def __repr__(self):
#         if self.left is None and self.right is None:
#             return str(self.value)
#         return pformat({"%s" % (self.value):(self.left, self.right)}, indent = 3)
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def __str__(self):
#         return str(self.root)
#
#     def is_empty(self):
#         return True \
#             if self.root is None \
#                 else False
#
#     def __insert(self, value):
#         node = Node(value, None)
#         if self.is_empty():
#             self.root = node
#         else:
#             parent = self.root
#             while True:
#                 if value < parent.value:
#                     if parent.left is None:
#                         parent.left = node
#                         break
#                     else:
#                         parent = parent.left
#                 elif value > parent.value:
#                     if parent.right is None:
#                         parent.right = node
#                         break
#                     else:
#                         parent = parent.right
#             node.parent = parent
#
#     def insert(self, *value):
#         for i in value:
#             self.__insert(i)
#         return self
#
#     def search(self, value):
#         if self.is_empty():
#             raise IndexError("空树无法查找")
#         else:
#             node = self.root
#             while node and node.value != value:
#                 node = node.left \
#                     if value < node.value \
#                         else node.right
#             return node
#
#     def is_right(self, node):
#         return node == node.parent.left
#
#     def remove(self, value):
#         if self.is_empty():
#             raise IndexError("树为空,无法删除")
#         else:
#             node = self.search(value)
#             if node is None:
#                 raise IndexError("查无此节点")
#             else:
#                 if node.left is None and node.right is None:
#                     self.__reassion(node, None)
#                 elif node.left:
#                     self.__reassion(node, node.left)
#                 elif node.right:
#                     self.__reassion(node, node.right)
#                 else:
#                     temp = self.get_max(node.left)
#                     self.remove(temp.value)
#                     node.value = temp.value
#
#     def __reassion(self, node, param):
#         if param is not None:
#             node.parent = param.parent
#         if node.parent is not None:
#             if self.is_right(node):
#                 node.parent.right = param
#             else:
#                 node.parent.left = param
#         else:
#             self.root = param
#     def get_max(self, left):
#         if left is None:
#             left = self.root
#         if not self.is_empty():
#             while left.right is not None:
#                 left = left.right
#         return left
#
#
# if __name__ == '__main__':
#     binarysearchtree = BST().insert(8,3,6,1)
#     print(binarysearchtree)
#     res = binarysearchtree.search(1)
#     print(res)


from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (
            self.left, self.right)}, indent=3)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        return True \
            if self.root \
            else False

    def __insert(self, value):
        node = Node(value, None)
        if self.is_empty():
            self.root = node
        else:
            while True:
                if value < node.value:
                    if node.left is None:
                        node.left = node
                        break
                    else:
                        node = node.left
                elif value > node.value:
                    if node.right is None:
                        node.right = node
                        break
                    else:
                        node = node.right
