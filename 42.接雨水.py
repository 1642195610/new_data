"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


from typing import List


def trap(height: List[int]) -> int:
    # 初始化一些变量,结果,数组长度
    ans = 0
    size = len(height)
    # 外层循环,遍历每个位置
    for i in range(size):
        leftmax = 0  # 记录每个位置对应的左侧最大值
        rightmax = 0  # 记录每个位置对应的右侧最大值
        for j in range(i, size):  # 找到当前位置右边最高的柱子,并记录下来
            rightmax = max(height[j], rightmax)
        for j in range(i, -1, -1):  # 找到当前位置左边最高的柱子,并记录下来
            leftmax = max(height[j], leftmax)
        # 计算当前位置能存多少雨水,并累加到结果上
        ans = ans + min(leftmax, rightmax) - height[i]
    return ans


if __name__ == '__main__':
    j = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(j))


def trap1(height: List[int]) -> int:
    if not height:
        return 0
    n = len(height)
    left = 0
    right = n - 1
    ans = 0
    l_max = height[0]
    r_max = height[n - 1]
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            ans += l_max - height[left]
            left += 1
        elif l_max >= r_max:
            ans += r_max - height[right]
            right -= 1
    return ans


if __name__ == '__main__':
    j = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap1(j))
