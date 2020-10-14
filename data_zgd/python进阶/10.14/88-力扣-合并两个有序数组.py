# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6], n = 3
from typing import List


class Solution:
    def merger_two(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    result = s.merger_two(nums1,m,nums2,3)
    print(result)


