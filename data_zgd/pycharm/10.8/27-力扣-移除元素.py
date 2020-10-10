from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = val
        # return nums # 查看数组
        return slow


if __name__ == "__main__":
    array = [0, 1, 2, 2, 3, 0, 4, 2]
    s = Solution()
    result = s.remove_element(array, 2)
    print(result)
