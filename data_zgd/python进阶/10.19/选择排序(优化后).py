from typing import List
from randomList import randomList


def sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        f = 1
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
                f = 0
        if f == 1:
            continue
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
        print(f"第{i + 1}轮排序结果: {nums}")
    return nums


if __name__ == '__main__':
    a = randomList.randomList(10)
    print(f"原始数组: {a}")
    res = sort(a)
    print(f"完成数组: {res}")
