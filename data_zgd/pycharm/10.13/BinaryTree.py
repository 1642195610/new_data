class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f"({self.data})"


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item):
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = new_node
                    return
                elif pop_node.right is None:
                    pop_node.right = new_node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def get_parent(self, item):
        if self.root == item:
            return IndexError("根节点没有父节点")
        else:
            temp = [self.root]
            while temp:
                pop_node = temp.pop(0)
                if pop_node.left.data == item:
                    return pop_node
                if pop_node.right.data == item:
                    return pop_node
                if pop_node.left:
                    temp.append(pop_node.left)
                if pop_node.right.data == item:
                    temp.append(pop_node.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    print(f"根节点: {bt.root}")
    print(f"根节点的左孩子: {bt.root.left}")
    print(f"根节点的右孩子: {bt.root.right}")
    print(f"根节点的左左孩子: {bt.root.left.left}")
    index = 3
    print(f"({index})的父节点: {bt.get_parent(index)}")
