class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        cur = self.head
        s = ""
        while cur:
            s += f"{cur},"
            cur = cur.next
        return "<" + str(s)[0:-1] + ">"

    def enqueue(self, data):
        new_data = Node(data)
        if self.is_entmy():
            self.head = new_data
            self.tail = new_data
        else:
            self.tail.next = new_data
            self.tail = new_data
        self.size += 1

    def dequeue(self):
        if self.is_entmy():
            raise IndexError("队列为空")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
        self.size -= 1
        return temp

    def is_entmy(self):
        return self.head is None


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"队列: {queue}")
    print(f"出队列的元素: {queue.dequeue()}")
    print(f"出队列后: {queue}")
