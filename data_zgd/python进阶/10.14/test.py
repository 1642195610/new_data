class Solution:
    # def two_sum(self, nums, target):
    #     for i in range(len(nums) - 1):
    #         for j in range(len(nums[i + 1:]),len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    def two_sum2(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [dic[temp],i]
            else:
                dic[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    # result = s.two_sum([3,3],6)
    # print(result)
    result2 = s.two_sum2([3,3],6)
    print(result2)