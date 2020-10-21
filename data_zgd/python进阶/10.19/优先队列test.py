class Queue:
    def __init__(self):
        self.size = 0
        self.array = []

    def enqueue(self, value):
        self.array.append(value)
        self.size += 1
        self.heapify_up()

    def dequeue(self):
        if self.size <= 0:
            raise Exception("空队列")
        remove_value = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapify_down()
        return remove_value

    def heapify_up(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) >> 1
        new = self.array[child_index]
        while child_index > 0 and new > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) >> 1
        self.array[child_index] = new

    def heapify_down(self):
        index = 0
        total_index = self.size - 1
        while True:
            maxvalue_index = index
            if 2 * index + 1 <= total_index and \
                self.array[2 * index + 1] > \
                    self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and \
                self.array[2 * index + 2] > \
                    self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.array[index],self.array[total_index] = \
            self.array[total_index],self.array[index]
            index = maxvalue_index


if __name__ == '__main__':
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(2)
    q.enqueue(7)
    print(q.array)
    print(q.dequeue())
    print(q.array)
