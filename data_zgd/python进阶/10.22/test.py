from randomList import randomList


# 归并排序
def merge(left, right):
    l_len = len(left)
    r_len = len(right)
    l = 0
    r = 0
    result = []
    while l < l_len and r < r_len:
        if left[l] < right[r]:
            result += [left[l]]
            l += 1
        else:
            result += [right[r]]
            r += 1
    if left:
        result += left[l:]
    if right:
        result += right[r:]
    return result


def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[0:mid], nums[mid:]
    return merge(mergesort(left), mergesort(right))


def merge2(left, right):
    l = 0
    r = 0
    result = []
    while left and right:
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if left:
        result.extend(left[l:])
    if right:
        result.extend(right[r:])
    return result


def mergesort2(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[0:mid], nums[mid:]
    return merge(mergesort(left), mergesort(right))


if __name__ == '__main__':
    list1 = randomList.randomList(10)
    print(f"未排序: {list1}")
    result = mergesort(list1)
    print(f"排序后: {result}")
    print(f"未排序: {list1}")
    result2 = mergesort2(list1)
    print(f"排序后: {result2}")
    print()


# 快速排序
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


def quick_sort(list, start, end):
    if start >= end:
        return
    mid = partition(list, start, end)
    quick_sort(list, start, mid - 1)
    quick_sort(list, mid + 1, end)


if __name__ == '__main__':
    list1 = randomList.randomList(10)
    print(f"未排序: {list1}")
    quick_sort(list1, 0, len(list1) - 1)
    print(f"排序后: {list1}")


# 移动零
def move_zero(nums):
    f = 0
    s = 0
    while f < len(nums):
        if nums[f] != 0:
            f += 1
        else:
            nums[f] = nums[s]
            s += 1
            f += 1
    for i in range(len(nums[f:])):
        nums[i] = 0
    return nums


if __name__ == '__main__':
    list1 = [1, 2, 3, 0, 3, 0, 4]
    print()
    print(list1)
    result = move_zero(list1)
    print(result)
