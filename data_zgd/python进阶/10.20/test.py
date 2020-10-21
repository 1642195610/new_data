from typing import List
from randomList import randomList


def sort(nums: List[int]) -> List[int]:  # 冒泡排序法
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        f = 1
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] \
                    = nums[j + 1], nums[j]
                f = 0
        if f == 1:
            break
        print(f"第{i + 1}轮排序结果: {nums}")
    return nums


if __name__ == '__main__':
    list = randomList.randomList(10)
    print(f"冒泡原始数据: {list}")
    result = sort(list)
    print(f"冒泡排序数据: {result}")
    print()


def sort1(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        maxindex = i
        f = 1
        for j in range(i + 1, len(nums)):
            if nums[maxindex] > nums[j]:
                maxindex = j
                f = 0
        if f:
            continue
        if maxindex != i:
            nums[i], nums[maxindex] = nums[maxindex], nums[i]
        print(f"第{i + 1}轮排序结果: {nums}")
    return nums


if __name__ == '__main__':
    list = randomList.randomList(10)
    print(f"选择原始数据: {list}")
    result1 = sort1(list)
    print(f"选择排序数据: {result1}")


def two_sum(nums: List[int], target: int):
    dict1 = {}
    for i in range(len(nums)):
        left = target - nums[i]
        if left in dict1:
            return [dict1[left], i]
        else:
            dict1[nums[i]] = i


if __name__ == '__main__':
    list = [2, 3, 7, 9]
    result = two_sum(list, 9)
    print(result)
