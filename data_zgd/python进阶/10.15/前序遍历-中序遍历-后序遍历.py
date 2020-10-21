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
        return pformat({"%s" % (self.value): (
            self.left, self.right)}, indent=3)


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
            root_node = self.root
            while True:
                if value < root_node.value:
                    if root_node.left is None:
                        root_node.left = insert_node
                        break
                    else:
                        root_node = root_node.left
                elif value > root_node.value:
                    if root_node.right is None:
                        root_node.right = insert_node
                        break
                    else:
                        root_node = root_node.right
            insert_node.parent = insert_node

    def insert(self, *value):
        for i in value:
            self.__insert(i)
        return self

    def is_empty(self):
        return True if self.root is None else False

    def pre_order_traverse(self, node): #递归-前序
        if not node:
            return None
        print(node.value, end=" -> ")
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    def pre_center_traverse(self, node): # 递归-中序
        if not node:
            return None
        self.pre_center_traverse(node.left)
        print(node.value,end=" -> ")
        self.pre_center_traverse(node.right)

    def pre_hou_traverse(self, node): # 递归-后序
        if not node:
            return None
        self.pre_hou_traverse(node.left)
        self.pre_hou_traverse(node.right)
        print(node.value,end=" -> ")

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

    def pre_hou_traverse2(self, node): # 栈-后序
        if node is None:
            return None
        else:
            stack1 = []
            stack2 = []
            stack1.append(node)
            while stack1:
                node = stack1.pop()
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
                stack2.append(node)
            while stack2:
                print(stack2.pop().value,end=" -> ")

    def level_order(self, node):
        if self.is_empty():
            raise IndexError("树为空")
        else:
            stack = [node]
            while stack:
                pop_node = stack.pop(0)
                print(pop_node.value,end=" -> ")
                if pop_node.left:
                    stack.append(pop_node.left)
                if pop_node.right:
                    stack.append(pop_node.right)


if __name__ == '__main__':
    bst = BinarySearchTree().insert(8, 3, 1, 6,10)
    print(bst)
    print(f"前序递归: ",end="")
    bst.pre_order_traverse(bst.root)
    print()
    print(f"中序递归: ",end="")
    bst.pre_center_traverse(bst.root)
    print()
    print(f"后序递归: ",end="")
    bst.pre_hou_traverse(bst.root)
    print()
    print(f"  前序栈: ",end="")
    bst.pre_order_traverse2(bst.root)
    print()
    print(f"  中序栈: ",end="")
    bst.pre_center_traverse2(bst.root)
    print()
    print(f"  后序栈: ",end="")
    bst.pre_hou_traverse2(bst.root)
    print()
    print(f"  层序栈: ",end="")
    bst.level_order(bst.root)
