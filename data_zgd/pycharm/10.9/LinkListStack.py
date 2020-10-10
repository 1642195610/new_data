class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def __repr__(self):
        return f"{self.val}"


class LinkListStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        curr = self.top
        s = ""
        while curr:
            s += f"{curr} <- "
            curr = curr.next
        return s + "top"

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("栈为空,无法弹出")
        else:
            pop_node = self.top
            self.top = pop_node.next
            pop_node.next = None
            self.size -= 1
        return pop_node

    def peek(self):
        return self.top

    def sizeof(self):
        return self.size

    def is_empty(self):
        return not bool(self.top)


lls = LinkListStack()
for i in range(4):
    lls.push(i)
print(f"压栈为: {lls}")
print(f"栈大小为: {lls.sizeof()}")
print(f"栈顶为: {lls.peek()}")
print(f"栈是否为空: {lls.is_empty()}")
print("弹栈为: ", end="")
for i in range(4):
    print(lls.pop(), end=" -> ")
print("None")
print(f"栈大小为: {lls.sizeof()}")
print(f"栈顶为: {lls.peek()}")
print(f"栈是否为空: {lls.is_empty()}")
