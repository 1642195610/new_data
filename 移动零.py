# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        f = 0
        while f < len(nums):
            if nums[f] == 0:
                f += 1
            else:
                nums[s] = nums[f]
                s += 1
                f += 1
        for i in range(s,len(nums)):
            nums[i] = 0
        return nums

if __name__ == '__main__':
    j = Solution()
    print(j.moveZeroes([0,1,0,3,12]))
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.最一开始快慢指针都是指向第一个
# 2.循环条件是快指针<数组长度
# 3.注意快指针!=给定值才赋值
# 4.注意最后不要忘记给后面元素赋值0


