from pprint import pformat


class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value):(self.left,self.right)},indent = 3)


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def __insert(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.root = new_node
        else:
            parent = self.root
            while True:
                if value < parent.value:
                    if parent.left is None:
                        parent.left = new_node
                        break
                    else:
                        parent = parent.left
                else:
                    if parent.right is None:
                        parent.right = new_node
                        break
                    else:
                        parent = parent.right

    def is_empty(self):
        return True if self.root is None else False

    def pre_order(self, node):
        if node is None:
            return None
        else:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return None
        else:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    def order(self, node):
        if node is None:
            return None
        else:
            self.order(node.left)
            self.order(node.right)
            print(node.value)

