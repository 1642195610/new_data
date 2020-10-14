from typing import List


class Solution:  # 方法一
    def remove_duplicated(self, nums: List[int]) -> int:
        n = len(set(nums))
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                temp = nums[i + 1]
                nums[i + 1:len(nums) - 1] = nums[i + 2:]
                nums[-1] = temp
                continue
            else:
                i += 1
        return i + 1


class Solution2:  # 方法二
    def remove_duplicated2(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
        return slow + 1


if __name__ == "__main__":
    array = [1, 1, 2, 2, 3, 4]
    s = Solution()
    result = s.remove_duplicated(array)
    print(result)
    array2 = [1, 1, 2, 2, 3, 4]
    s2 = Solution2()
    result2 = s2.remove_duplicated2(array2)
    print(result2)
