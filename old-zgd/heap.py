class heap(object):

    def __init__(self):  # 初始化函数
        self.data_list = []  # 存放所有数据

    def get_parent_index(self, index: int):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        """
        交换两个索引对应的值
        :param index_a: a的索引
        :type index_a: int
        :param index_b: b的索引
        :type index_b: int
        :return:
        :rtype:
        """
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data: int):
        self.data_list.append(data)  # 把一个新元素插入到原有列表末尾
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2 * index + \
                    1 <= total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + \
                    2 <= total_index and self.data_list[2 * index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


if __name__ == '__main__':
    h = heap()
    for i in range(10):
        h.insert(i + 1)
    print("建堆: ", h.data_list)
    print("删顶: ", [h.pop() for _ in range(10)])
