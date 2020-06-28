from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0
        f = 0
        while f < len(nums):
            if nums[f] == val:
                f += 1
            else:
                nums[s] = nums[f]
                f += 1
                s += 1
        return s


if __name__ == '__main__':
    j = Solution()
    print(j.removeElement([3, 2, 2, 3], 3))
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.最一开始快慢指针都是指向第一个
# 2.循环条件是快指针<数组长度
# 3.注意快指针!=给定值才赋值