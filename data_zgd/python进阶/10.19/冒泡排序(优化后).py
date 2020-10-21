from typing import List
from randomList import randomList


def sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        f = 1
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                f = 0
        if f == 1:
            break
        print(f"第{i + 1}论排序结果: {nums}")
    return nums


if __name__ == '__main__':
    # a = [10, 20, 40, 5, 7, 90, 23, 34, 45, 56, 45, 56, 67, 34, 23]
    a = randomList.randomList(10)
    print(f"原始数组: {a}")
    res = sort(a)
    print(f"完成数组: {res}")
