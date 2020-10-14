from pprint import pformat


class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return pformat({"%s" % (self.value):(self.left,self.right)},indent=1)


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def __insert(self, value):
        new_node = Node(value, None)
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

    def insert(self,*value):
        for i in value:
            self.__insert(i)
        return self

    def is_empty(self):
        # if self.root is None:
        #     return True
        # else:
        #     return False
        return True if self.root is None else False

    def search(self, value):
        if self.is_empty():
            raise IndexError("二分搜索树为空,无法查找")
        else:
            new_node = self.root
            while new_node and new_node.value != value:
                # if value < new_node.value:
                #     new_node = new_node.left
                # elif value > new_node.value:
                #     new_node = new_node.right
                new_node = new_node.left if value < new_node.value \
                    else new_node.right
        return new_node


if __name__ == '__main__':
    bst = BST()
    res = bst.insert(8,3,6,1)
    print(res)
    print(bst.search(7))


