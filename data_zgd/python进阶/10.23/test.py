# 快排单指针-1
# 快排双指针-2
from randomList import randomList
import copy


def partition(list_list, start, end):
    pivot = list_list[start]
    mark = start
    for i in range(start + 1, end + 1):
        if list_list[i] < pivot:
            mark += 1
            list_list[mark], list_list[i] \
                = list_list[i], list_list[mark]
    list_list[start] = list_list[mark]
    list_list[mark] = pivot
    return mark


def quick_sort(list_list, start, end):
    if start >= end:
        return
    mid = partition(list_list, start, end)
    quick_sort(list_list, start, mid - 1)
    quick_sort(list_list, mid + 1, end)


def swap(list_list, p, q):
    list_list[p], list_list[q] \
        = list_list[q], list_list[p]


def partition2(list_list, start, end):
    pivot = list_list[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and list_list[p] < pivot:
            p += 1
        while p <= q and list_list[q] >= pivot:
            q -= 1
        if p < q:
            swap(list_list, p, q)
    swap(list_list, start, q)
    return q


def quick_sort2(list_list, start, end):
    if start >= end:
        return
    mid = partition(list_list, start, end)
    quick_sort2(list_list, start, mid - 1)
    quick_sort2(list_list, mid + 1, end)


def count_sort(list_list):
    dict1 = {}
    result1 = []
    z_result = []
    for i in range(len(list_list)):
        if list_list[i] not in result1:
            result1.append(list_list[i])
        if list_list[i] not in dict1:
            dict1[list_list[i]] = 1
        else:
            dict1[list_list[i]] += 1
    print(dict1)
    print(f"去重后: {result1}")
    list_copy = copy.deepcopy(result1)
    for i in range(len(result1)):
        min_value = min(list_copy)
        for j in range(dict1[min_value]):
            min_value = min(list_copy)
            z_result.append(min_value)
        list_copy.remove(min_value)
    return z_result


if __name__ == '__main__':
    list1 = randomList.randomList(10)
    print(list1)
    quick_sort(list1, 0, len(list1) - 1)
    print(list1)
    list1 = randomList.randomList(10)
    print(list1)
    quick_sort2(list1, 0, len(list1) - 1)
    print(list1)
    print()
    list1 = randomList.randomList(10)
    print(f"未排序: {list1}")
    result11 = count_sort(list1)
    print(f"排序后: {result11}")
