from typing import List


class Solution:
    def binary_search(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            if target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            else:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid
                elif target > nums[mid]:
                    left = mid
                else:
                    return mid

    def binary_search2(self, nums: List[int], target: int):
        left = -1
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid

    def binary_search3(self, nums: List[int], target: int):
        left = -1
        right = len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid



if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = s.binary_search(nums,target)
    print(result)
    result2 = s.binary_search2(nums,target)
    print(result2)
    result3 = s.binary_search3(nums,target)
    print(result3)