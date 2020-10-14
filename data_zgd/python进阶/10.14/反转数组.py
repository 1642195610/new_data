from typing import List


class Solution:
    def reverse(self, nums: List[int]):
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    list = list(range(1,10))
    print(list)
    result = s.reverse(list)
    print(result)