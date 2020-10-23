from randomList import randomList


def bucket_sort(list_list):
    max_value = max(list_list)
    min_value = min(list_list)
    d = max_value - min_value
    bucket_count = len(list_list)
    count_list = []  # 外桶
    for i in range(bucket_count):
        count_list.append([])  # 添加内筒空间
    for i in range(len(list_list)):
        # int((列表每一个数-最小值)*(桶数-1)/(最大值-最小值))
        index = int((list_list[i] - min_value) * (bucket_count - 1) / d)
        bucket = count_list[index]
        bucket.append(list_list[i])
    for i in range(len(count_list)):
        count_list[i].sort()
    result1 = []
    for wai in count_list:
        for nei in wai:
            result1.append(nei)
    return result1


if __name__ == '__main__':
    # list1 = [3, 3, 4, 1, 2, 3, 3, 4, 5, 5, 4, 6]
    list1 = randomList.randomList(10)
    print(list1)
    res = bucket_sort(list1)
    print(res)
