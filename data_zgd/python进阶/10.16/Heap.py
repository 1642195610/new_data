class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a],self.data_list[index_b] \
            = self.data_list[index_b],self.data_list[index_a]

    def insert(self, value):
        self.data_list.append(value)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and \
                self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def remove(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        maxvalue_index= index
        total_index = len(self.data_list) - 1
        while True:
            if 2 * index + 1 <= total_index and \
                self.data_list[2 * index + 1] > \
                    self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and \
                self.data_list[2 * index + 2] > \
                    self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(maxvalue_index, index)
            index = maxvalue_index


if __name__ == '__main__':
    h = Heap()
    h.insert(1)
    h.insert(3)
    h.insert(4)
    h.insert(2)
    print("建堆: ",end=" ")
    print(h.data_list)
    print("删堆: ",end=" ")
    for i in range(4):
        print(h.remove(),end=", ")