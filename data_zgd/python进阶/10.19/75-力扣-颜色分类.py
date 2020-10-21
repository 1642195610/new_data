"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        for i in range(len(nums) - 1):
            f = 1
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
                    f = 0
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
            if f == 1:
                continue
        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    s = Solution()
    result = s.sortColors(nums)
    print(result)


class Solution1:
    def sortColors1(self, nums: List[int]) -> None:
        a = c = 0
        b = len(nums) - 1
        while c <= b:
            if nums[c] == 0:
                nums[a], nums[c] = nums[c], nums[a]
                a += 1
                c += 1
            elif nums[c] == 2:
                nums[c], nums[b] = nums[b], nums[c]
                b -= 1
            else:
                c += 1
        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    s = Solution1()
    result = s.sortColors1(nums)
    print(result)
