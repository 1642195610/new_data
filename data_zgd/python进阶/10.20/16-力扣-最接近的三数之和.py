"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List



class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_value = float("inf")
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if abs(res - target) < min_value:
                    min_value = abs(res - target)
                    result = res
                if res > target:
                    right -= 1
                elif res < target:
                    left += 1
                else:
                    return res
        return result








    def three_sum_closest2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()  # 排序
        ans = float('inf')

        for first in range(n - 2):  # 枚举第一个元素
            if first > 0 and nums[first] == nums[first - 1]: continue  # 保证first不会有重复

            second, third = first + 1, n - 1
            max_sum = nums[first] + nums[-2] + nums[-1]
            min_sum = nums[first] + nums[first + 1] + nums[first + 2]
            if max_sum <= target:  # 最大的数
                if abs(max_sum - target) < abs(ans - target):
                    ans = max_sum
                continue
            elif min_sum >= target:  # 最小的数
                if abs(min_sum - target) < abs(ans - target):
                    ans = min_sum
                break

            while second < third:
                two_sum_target = target - nums[first]
                s = nums[second] + nums[third]
                if abs(s + nums[first] - target) < abs(ans - target):
                    ans = s + nums[first]
                if s > two_sum_target:  # 当前数值太大 右指针左移
                    third -= 1
                    while third > second and nums[third] == nums[third + 1]:
                        third -= 1
                elif s < two_sum_target:  # 当前数值太小 左指针右移
                    second += 1
                    while third > second and nums[second] == nums[second - 1]:
                        second += 1
                else:  # 刚好等于 直接返回target即可
                    return target

        return ans


if __name__ == '__main__':
    s = Solution()
    # nums = [1,1,1,0]
    nums = [1,-1,0,-9]
    target = 100
    result = s.three_sum_closest(nums, target)
    print(result)
    result2 = s.three_sum_closest2(nums, target)
    print(result2)

