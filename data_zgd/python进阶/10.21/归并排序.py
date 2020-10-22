from typing import List
from randomList import randomList


def merge(left, right):
    res = []
    while left and right:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res


def mergesort(nums: List[int]):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[0:mid], nums[mid:]
    return merge(mergesort(left), mergesort(right))


def merge2(left, right):
    result = []
    l_len = len(left)
    r_len = len(right)
    l = 0
    r = 0
    while l < l_len and r < r_len:
        if left[l] > right[r]:
            result += [right[r]]
            r += 1
        else:
            result += [left[l]]
            l += 1
    if left:
        result += left[l:]
    if right:
        result += right[r:]
    return result


def mergesort2(nums: List[int]):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[0:mid], nums[mid:]
    return merge2(mergesort2(left), mergesort2(right))


if __name__ == '__main__':
    list = randomList.randomList(10)
    result = mergesort(list)
    result2 = mergesort2(list)
    print(f"未排序数组: {list}")
    print(f"归并排序后: {result}")
    print(f"未排序数组: {list}")
    print(f"归并排序后: {result2}")
