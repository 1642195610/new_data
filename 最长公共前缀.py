# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。


from typing import List


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = ''#结果
#         for each in zip(*strs):#遍历字符串
#             if len(set(each)) == 1:#判断公共字符
#                 res += each[0]
#             else:
#                 return res#没有公共字符返回结果
#         return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minLength = min([len(s) for s in strs])
        publicWord = []
        for i in range(minLength):
            for word in strs:
                publicWord.append(word[:i + 1])
            if len(set(publicWord)) == 1:
                publicWord = []
            else:
                return strs[0][:i]
        if len(strs) <= 2:
            if len(strs[0]) == 1:
                return strs[0]
            elif len(strs[0]) == 2:
                i = min(len(strs[0]), len(strs[1]))
                return strs[0][:i]


if __name__ == '__main__':
    j = Solution()
    a = j.longestCommonPrefix(["flower", "flow", "flight"])
    print(a)
    a = j.longestCommonPrefix(["a"])
    print(a)
    a = j.longestCommonPrefix(["c", "c"])
    print(a)
    a = j.longestCommonPrefix(["aa", "a"])
    print(a)
    a = j.longestCommonPrefix(["aaa", "aa", "aaa"])
    print(a)


# a = [1,2,3]
# b = list(zip(a))
# print("原列表:",a)
# print("压缩后:",b)
# for each in zip(*b):
#     print("解压缩后:",each)
# a = [1, 2, 3]
# b = [4, 5, 6]
# zipped = list(zip(a, b))
# print(zipped)
# for each in zipped:
#     print(each)
#
# for each in zip(*zipped):
#     print(each)
#
# strs = ["flower", "flow", "flight"]
# minLength = min([len(s) for s in strs])
# print(minLength)


# def longestCommonPrefix(strs: List[str]):
#     if len(strs) == 0 or "" in strs:
#         return ""
#     if len(strs) == 1:
#         return strs
#     minLength = min([len(s) for s in strs])
#     publicWord = []
#     for i in range(minLength):
#         for word in strs:
#             publicWord.append(word[:i+1])
#         if len(set(publicWord)) == 1:
#             publicWord = []
#         else:
#             return strs[0][:i]
#
# ["flower", "flow", "flight"]
# def longCommonPrefix(strs: List[str]):
#     res = ''
#     for each in zip(*strs):
#         if len(set(each)) == 1:
#             res += each[0]
#         else:
#             return res
#     return res
#
#
# if __name__ == '__main__':
#     l = ["flower", "flow", "flight"]
#     print(longCommonPrefix(l))
#     print(longestCommonPrefix(l))
