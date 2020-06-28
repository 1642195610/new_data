from typing import List


class Solution:
    def removeDuplicated(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow +=1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.快指针先去探索
# 2.先满指针+=1,再把快指针的值赋值给满指针