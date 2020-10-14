class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.size = 0

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise IndexError("栈为空")
        return temp

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def sizeof(self):
        return self.size


if __name__ == "__main__":
    s = Stack(10)
    for i in range(4):
        s.push(i)
    print(f"压栈为: {s}")
    print(f"栈大小为: {s.sizeof()}")
    print(f"栈顶为: {s.peek()}")
    print(f"栈是否为空: {s.is_empty()}")
    print("弹栈为: ", end="")
    for i in range(4):
        print(s.pop(), end=" -> ")
    print("None")
    print(f"栈大小为: {s.sizeof()}")
    print(f"栈顶为: {s.peek()}")
    print(f"栈是否为空: {s.is_empty()}")
