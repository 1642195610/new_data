# 16.最接近的三数之和
# 给定一个包括 n 个整数的数组 nums 和一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#
#
# 示例：
#
# 输入：nums = [-1, 2, 1, -4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
# 提示：
#
# 3 <= nums.length <= 10 ^ 3
# -10 ^ 3 <= nums[i] <= 10 ^ 3
# -10 ^ 4 <= target <= 10 ^ 4


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
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.先要排序
# 2.一定不要忘记定义左右值