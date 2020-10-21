from pprint import pformat


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value):(self.left,self.right)}, indent = 3)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def __insert(self, value):
        insert_node = Node(value)
        if self.is_empty():
            self.root = insert_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = insert_node
                        break
                    else:
                        parent_node = parent_node.left
                elif value > parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = insert_node
                        break
                    else:
                        parent_node = parent_node.right

    def insert(self, *value):
        for i in value:
            self.__insert(i)
        return self

    def is_empty(self):
        return True if self.root is None else False

    def search(self, value):
        if self.is_empty():
            raise IndexError("树为空")
        else:
            search_node = Node(value)
            if search_node is None:
                raise IndexError("查无此节点")
            else:
                parent_node = self.root
                while True:
                    if parent_node and value != parent_node.value:
                        if value < parent_node.value:
                            parent_node = parent_node.left
                        elif value > parent_node.value:
                            parent_node = parent_node.right
                        return parent_node

    def remove(self, value):
        if self.is_empty():
            raise IndexError("树为空")
        else:
            search_node = self.search(value)
            if search_node is None:
                raise IndexError("查无此节点,无法删除")
            else:
                if search_node.left is None and search_node.right is None:
                    self.__reassion(search_node,None)
                elif search_node.left:
                    self.__reassion(search_node, search_node.left)
                elif search_node.right:
                    self.__reassion(search_node, search_node.right)
                else:
                    temp = self.get_max(search_node.left)
                    self.remove(temp.value)
                    search_node.value = temp.value

    def __reassion(self, parent, child):
        if child is not None:
            child.parent = parent.parent
        if parent.parent is not None:
            if self.is_right(parent):
                parent.right = child
            else:
                parent.left = child
        else:
            self.root = child

    def get_max(self, left_node):
        if left_node is None:
            left_node = self.root
        if not self.is_empty():
            while left_node.right is not None:
                left_node = left_node.right
        return left_node


    def is_right(self,node):
        return node == node.parent.left

    def pre_order_traverse2(self, node): # 栈-前序
        stack = [node]
        while len(stack) > 0:
            print(node.value,end=" -> ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def pre_center_traverse2(self, node): # 栈-中序
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value,end=" -> ")
                node = node.right

    def pre_order(self, node): # 递归-前序
        if node is None:
            return None
        print(node.value, end=" -> ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node): #递归-中序
        if node is None:
            return None
        self.in_order(node.left)
        print(node.value, end=" -> ")
        self.in_order(node.right)

    # 前序: pre_order
    # 中序: in_order
    # 后序: post_order


if __name__ == '__main__':
    bst = BinarySearchTree().insert(8,3,6,1,10)
    print(bst)
    print(bst.search(3))
    print("栈前序: ",end=" ")
    bst.pre_order_traverse2(bst.root)
    print()
    print("栈中序: ",end=" ")
    bst.pre_center_traverse2(bst.root)
    print()
    print("递归前序: ",end=" ")
    bst.pre_order(bst.root)
    print()
    print("递归中序: ",end=" ")
    bst.in_order(bst.root)
    print()
    bst.remove(1)
    print(bst)
