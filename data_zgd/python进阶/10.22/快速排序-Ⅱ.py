from randomList import randomList


# 单指针遍历法
def partition(list_list, start, end):
    pivot = list_list[start]
    mark = start
    for i in range(start + 1, end + 1):
        if list_list[i] < pivot:
            mark += 1
            list_list[mark], list_list[i] = list_list[i], list_list[mark]
    list_list[start] = list_list[mark]
    list_list[mark] = pivot
    return mark


def quick_sort(list_list, start, end):
    if start >= end:
        return
    mid = partition(list_list, start, end)
    quick_sort(list_list, start, mid - 1)
    quick_sort(list_list, mid + 1, end)


if __name__ == '__main__':
    list1 = randomList.randomList(10)
    print(list1)
    quick_sort(list1, 0, len(list1) - 1)
    print(list1)
