class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0:
            raise IndexError("数组越界")
        if index >= len(self.array) or self.size >= len(self.array):
            self.add_capacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("数组越界")
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def add_capacity(self):
        new_array = [None] * len(self.array) * 2  # 创建一个新的数组
        for i in range(self.size):
            new_array[i] = self.array[i]  # 把旧数组的值赋值给新数组
        self.array = new_array  # 使用新数组

    def out_put(self):
        print(self.array)
        # s = ""
        # for i in range(self.size):
        #     s += f" {self.array[i]} "
        # return "[" + s + "]"


array = Array(4)
array.insert(0, 0)
array.insert(1, 1)
array.insert(2, 2)
array.insert(0, 10)
array.insert(4, 30)
array.insert(2, 100)
array.insert(7, 700)
array.out_put()
print(array.out_put())
array.remove(0)
array.out_put()
array.remove(4)
array.out_put()
array.remove(1)
array.out_put()
