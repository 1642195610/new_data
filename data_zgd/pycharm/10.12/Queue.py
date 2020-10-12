class Queue:
    def __init__(self):
        self.entries = []
        self.size = 0

    def __repr__(self):
        return "<" + str(self.entries)[1:-1] + ">"

    def enqueue(self, data):
        self.entries.append(data)
        self.size += 1

    def dequeue(self):
        temp = self.entries[0]
        self.entries = self.entries[1:]
        self.size -= 1
        return temp

    def size(self):
        return self.size

    def get(self, index):
        return self.entries[index]

    def reverse(self):
        self.entries = self.entries[::-1]


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(f"队列: {queue}")
    print(f"删除的队列元素: {queue.dequeue()}")
    print(f"删除后的队列: {queue}")
    print(f"队列的大小: {queue.size}")
    index = 1
    print(f"查找的队列元素位置: {index}\n查找的队列元素为: {queue.get(index)}")
    queue.reverse()
    print(f"倒序后的队列: {queue}")