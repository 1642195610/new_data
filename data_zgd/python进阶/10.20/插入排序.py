from typing import List
from randomList import randomList


class Solution:
    def insert_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        for right in range(1, len(nums)):
            target = nums[right]
            for left in range(0, right):
                if nums[left] > target:
                    nums[left + 1: right + 1] = \
                        nums[left: right]
                    nums[left] = target
                    break
            print(f"第{right}轮排序结果: {nums}")
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = randomList.randomList(10)
    print(f"插入原始数据: {nums}")
    result = s.insert_sort(nums)
    print(f"插入排序完成: {result}")
