from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (
            self.left, self.right)}, indent=1)
        # 结点:(结点的左孩子,结点的右孩子)


class Bst:
    def __init__(self, root=None):
        self.root = root  # self.read

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __str__(self):
        return str(self.root)

    def is_right(self, node):
        return node == node.parent.right

    def find(self, value):
        if self.is_empty():
            raise IndexError("空树不要查找了,找也找不到哒!!!")
        else:
            node = self.root
            while node and node.value != value:
                node = node.left if value < node.value else node.right
            # print(node)
            return node

    def remove(self, value: int):
        search_node = self.find(value)
        if search_node is not None:
            if search_node.left is None and search_node.right is None:
                self.__reassign_nodes(search_node, None)
            elif search_node.left is None:
                self.__reassign_nodes(search_node, search_node.right)
            elif search_node.right is None:
                self.__reassign_nodes(search_node, search_node.left)
            else:
                temp = self.get_max(search_node.left)
                self.remove(temp.value)
                search_node.value = temp.value
        return search_node.value

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def __insert(self, value):
        new_node = Node(value, None)  # 创建新结点
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *args):
        for value in args:
            self.__insert(value)
        return self.root
    # 前序遍历:

    def fater(self, node):
        if node is None:
            return
        print("%s" % node.value, end=" ")
        self.fater(node.left)
        self.fater(node.right)
        return node

    # 中序遍历:
    def center(self, node):
        if node is None:
            return
        self.center(node.left)
        print("%s" % node.value, end=" ")
        self.center(node.right)
        return node

    # 后序遍历:
    def not_fater(self, node):
        if node is None:
            return
        self.not_fater(node.left)
        self.not_fater(node.right)
        print("%s" % node.value, end=" ")
        return node


if __name__ == '__main__':
    j = Bst()
    a = j.insert(2, 5, 4, 7, 9)
    print("删除前树为: %s" % a)
    print("查找的树为: %s" % j.find(4))
    # print("删除的树为: %s" % j.remove(4))
    print("删除后树为: %s" % a)
    print("前序遍历为: 中左右: %s" % a, end=" ")
    j.fater(j.root)
    print()
    print("中序遍历为: 左中右: %s" % a, end=" ")
    j.center(j.root)
    print()
    print("后序遍历为: 左右中: %s" % a, end=" ")
    j.not_fater(j.root)


# from pprint import pformat
#
#
# class Node:
#     def __init__(self,value,parent):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.parent = parent
#
#     def __repr__(self):
#         if self.left is None and self.right is None:
#             return str(self.value)
#         else:
#             return pformat({"%s"%(self.value):(self.left,self.right)},indent=3)
#
#
# class Bst:
#     def __init__(self,root = None):
#         self.root = root
#
#     def is_empty(self):
#         if self.root is None:
#             return True
#         return False
#
#     def __str__(self):
#         return str(self.root)
#
#     def is_right(self,node):
#         return node == node.parent.right
#
#     def __insert(self,value):
#         new_node = Node(value,None)
#         if self.is_empty():
#             self.root = new_node
#         else:
#             parent_node = self.root
#             while True:
#                 if value < parent_node.value:
#                     if parent_node.left is None:
#                         parent_node.left = new_node
#                         break
#                     else:
#                         parent_node = parent_node.left
#                 elif value >= parent_node.value:
#                     if parent_node .right is None:
#                         parent_node.right = new_node
#                         break
#                     else:
#                         parent_node = parent_node.right
#             new_node.parent = parent_node
#
#     def insert(self,*args):
#         for value in args:
#             self.__insert(value)
#         return self.root
#
#
# if __name__ == '__main__':
#     j = Bst()
#     a = j.insert(8,5,10,6,4)
#     print("删除前树为: %s"%a)


# from pprint import pformat
#
#
# class Node:
#     def __init__(self,value,parent):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.parent = parent
#
#     def __repr__(self):
#         if self.left is None and self.right is None:
#             return str(self.value)
#         return pformat({"%s"%(self.value):(self.left,self.right)},indent=3)
#
#
# class Bst:
#     def __init__(self,root=None):
#         self.root = root
#
#     def is_empty(self):
#         if self.root is None:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return str(self.root)
#
#     def is_right(self,node):
#         return node == node.parent.right
#
#     def __insert(self,value):
#         new_node = Node(value,None)
#         if self.is_empty():
#             self.root = new_node
#         else:
#             parent_node = self.root
#             while True:
#                 if value < parent_node.value:
#                     if parent_node.left is None:
#                         parent_node.left = new_node
#                         break
#                     else:
#                         parent_node = parent_node.left
#                 elif value >= parent_node.value:
#                     if parent_node.right is None:
#                         parent_node.right = new_node
#                         break
#                     else:
#                         parent_node = parent_node.right
#             new_node.parent = parent_node
#
#     def insert(self,*args):
#         for value in args:
#             self.__insert(value)
#         return self.root
#
#     def find(self,value):
#         if self.is_empty():
#             raise IndexError("空树就不要查找啦,找也找不到哒!!!")
#         else:
#             node = self.root
#             while node and node.value != value:
#                node = node.left if value < node.value else node.right
#             return node
#
#
# if __name__ == '__main__':
#     j = Bst()
#     z = j.insert(9,7,1,5,6,0)
#     print("原二分查找树: ",format(z))
#     print("要查找的值为: ",format(j.find(0)))
