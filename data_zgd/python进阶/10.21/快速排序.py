from randomList import randomList


def swap(list, start, q):
    list[start], list[q] = list[q], list[start]


def partition(list, start, end):
    poivt = list[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and list[p] < poivt:
            p += 1
        while p <= q and list[q] >= poivt:
            q -= 1
        if p < q:
            swap(list, p, q)
    swap(list, start, q)
    return q


def quicksort(list, start, end):
    if start >= end:
        return
    mid = partition(list, start, end)
    quicksort(list, start, mid - 1)
    quicksort(list, mid + 1, end)


if __name__ == '__main__':
    list = randomList.randomList(10)
    print(list)
    result = quicksort(list, 0, len(list) - 1)
    print(list)
