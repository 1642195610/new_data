class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def put(self,item):
        self.entries.append(item)
        self.length += 1

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[1:]
        return dequeued

    def rotate(self,rotation):
        for i in range(rotation):
            self.put(self.get())

    def front(self):
        return self.entries[0]

    def size(self):
        return self.length


q = Queue()
q.put(1)
q.put(2)
q.put(3)
print(q)
print(q.get())
print(q)