"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0

    def minSubArrayLen2(self, s: int, nums: List[int]) -> int: # 滑动窗口
        left, sum, res = 0, 0, float("inf")
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= s:
                length = right - left + 1
                if length < res:
                    res = length
                sum -= nums[left]
                left += 1
        return res if res != float("inf") else 0


if __name__ == '__main__':
    s = Solution()
    s_int = 7
    nums = [2, 3, 1, 2, 4, 3]
    result = s.minSubArrayLen(s_int, nums)
    print(result)
    result2 = s.minSubArrayLen2(s_int, nums)
    print(result2)
