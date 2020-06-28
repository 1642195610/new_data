from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in dict:
                return [dict[t],i]
            else:
                dict[nums[i]] = i

if __name__ == '__main__':
    j = Solution()
    print(j.twoSum([2, 7, 11, 15], 9))
# ————————————————
# 版权声明：本文为CSDN博主「姜泽毓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43722162/article/details/106992220


# 注意:
# 1.字典里面存放的是值不是下标