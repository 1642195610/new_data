class Solution:
    def two_sum(self,nums,target):
        num = nums.copy()
        nums.sort()
        begin = 0
        end = len(nums) - 1
        b = nums[begin]
        e = nums[end]
        while begin < end:
            cur = nums[begin] + nums[end]
            if cur == target:
                b= nums[begin]
                e = nums[end]
                begin += 1
                end -= 1
            else:
                if cur < target:
                    begin += 1
                else:
                    end -= 1
        if b != e:
            for i in range(len(num)):
                if num[i] == b:
                    bb = i
                if num[i] == e:
                    ee = i
            return [ee,bb]


if __name__ == '__main__':
    s = Solution()
    # nums = [3,4,2]
    nums = [3,3]
    target = 6
    res = s.two_sum(nums,target)
    print(res)