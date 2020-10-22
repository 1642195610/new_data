from randomList import randomList


# 单指针遍历法
def partition(list, start, end):
    pivot = list[start]
    mark = start
    for i in range(start + 1, end + 1):
        if list[i] < pivot:
            mark += 1
            list[mark], list[i] = list[i], list[mark]
    list[start] = list[mark]
    list[mark] = pivot
    return mark


def quicksort(list, start, end):
    if start >= end:
        return
    mid = partition(list, start, end)
    quicksort(list, start, mid - 1)
    quicksort(list, mid + 1, end)


if __name__ == '__main__':
    list = randomList.randomList(10)
    print(list)
    quicksort(list, 0, len(list) - 1)
    print(list)
