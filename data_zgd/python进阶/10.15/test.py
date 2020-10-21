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

    def __insert(self, value):
        new_node = Node(value, None)
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
                elif value > parent.value:
                    if parent.right is None:
                        parent.right = new_node
                        break
                    else:
                        parent = parent.right
            new_node.parent = parent

    def insert(self, *value):
        for i in value:
            self.__insert(i)
        return self

    def is_empty(self):
        return True \
            if self.root is None \
            else False

    def search(self, value):
        if self.is_empty():
            raise IndexError("树为空,无法查找")
        else:
            parent = self.root
            while parent and parent.value != value:
                if value < parent.value:
                    parent = parent.left
                elif value > parent.value:
                    parent = parent.right
            return parent

    def remove(self, value):
        if self.is_empty():
            raise IndexError("树为空")
        else:
            search = self.search(value)
            if search is None:
                raise IndexError("查无此节点")
            else:
                if search.left is None and search.right is None:
                    self.__reassion(search, None)
                elif search.left:
                    self.__reassion(search, search.left)
                elif search.right:
                    self.__reassion(search, search.right)
                else:
                    temp = self.get_max(search.left)
                    self.remove(temp.value)
                    search.value = temp.value

    def __reassion(self, value, param):
        if param is not None:
            param.parent = value.parent
        if value.parent is not None:
            if self.is_right(value):
                value.right = param
            else:
                value.left = param
        else:
            self.root = param

    def is_right(self, left):
        return left == left.parent.left

    def get_max(self, value):
        if value is None:
            value = self.root
        if not self.is_empty():
            while value.right is not None:
                value = value.right
        return value


if __name__ == '__main__':
    bst = BinarySearchTree().insert(8, 3, 6, 1)
    print(bst)
    print(bst.search(3))
    bst.remove(1)
    print(bst)
    bst.remove(3)
    print(bst)
    bst.remove(6)
    print(bst)
    bst.remove(8)
    print(bst)
