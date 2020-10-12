class Node:
    def __init__(self, data):
        self.queue = []
        self.size = 0

    def __repr__(self):
        printed = "<" + str(self.queue)[1:-1] + ">"
        return printed

    def put(self, data):
        self.queue.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("队列为空,无法出队列")
        else:
