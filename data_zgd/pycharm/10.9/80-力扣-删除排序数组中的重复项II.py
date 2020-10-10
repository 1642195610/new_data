from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        count = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                count = 1
            else:
                count += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
                fast += 1
        return slow + 1


if __name__ == "__main__":
    array = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s = Solution()
    result = s.remove_duplicates(array)
    print(result)
