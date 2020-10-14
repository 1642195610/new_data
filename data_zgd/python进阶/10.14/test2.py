from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value) \
            if self.left is None and self.right is None \
            else pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        return True if self.root is None \
            else False

    def __insert(self, data):
        new = Node(data, None)
        if self.is_empty():
            self.root = new
        else:
            parent = self.root
            while True:
                if data < parent.value:
                    if parent.left is None:
                        parent.left = new
                        break
                    else:
                        parent = parent.left
                elif data > parent.value:
                    if parent.right is None:
                        parent.right = new
                        break
                    else:
                        parent = parent.right
            new.parent = parent

    def insert(self, *data):
        for i in data:
            self.__insert(i)
        return self

    def search(self, data):
        if self.is_empty():
            raise IndexError("空树无法查找")
        else:
            new = self.root
            while new and new.value != data:
                new = new.left if data < new.value \
                    else new.right
            return new

    def remove(self, value):
        if self.root is None:
            raise IndexError("树为空,无法删除")
        else:
            node = self.search(value)
            if node is None:
                raise IndexError("无此节点,无法删除")
            elif node is not None:
                if node.left is None and node.right is None:
                    self.__reassion(node, None)
                elif node.left is not None:
                    self.__reassion(node, node.right)
                elif node.right is not None:
                    self.__reassion(node, node.left)
                else:
                    temp = self.get_max(node.left)
                    self.remove(temp.value)
                    node.value = temp.value

    def __reassion(self, node, child):
        if child is not None:
            node.parent = child.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = child
            else:
                node.parent.left = child
        else:
            self.root = child

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def is_right(self, node):
        return node == node.parent.right


if __name__ == '__main__':
    bst = BST().insert(8, 3, 6, 1)
    print(bst)
    print(bst.search(6))
