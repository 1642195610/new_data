from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in dict1:
                return [dict1[left], i]
            else:
                dict1[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 4]
    target = 6
    res = s.two_sum(nums, target)
    print(res)