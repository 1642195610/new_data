from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min = abs(nums[0] + nums[1] + nums[2] - target)
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(sum - target) < min:
                    min = abs(sum - target)
                    res = sum
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return sum
        return res


if __name__ == '__main__':
    l = [-1, 2, 1, -4]
    j = Solution()
    a = j.threeSumClosest(l, 1)
    print(a)
