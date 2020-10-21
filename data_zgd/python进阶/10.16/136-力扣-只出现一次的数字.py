from typing import List

# [2,2,1]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res


if __name__ == '__main__':
    s = Solution()
    num = [4,2,1,2,1]
    print(s.singleNumber(num))
