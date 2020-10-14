from typing import List


class Solution:
    def move_zero(self, nums: List[int]) -> List:
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums


if __name__ == '__main__':
    array = [0, 1, 0, 3, 12]
    s = Solution()
    a = s.move_zero(array)
    print(a)
