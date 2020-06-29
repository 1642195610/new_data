# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        maxlen = 1
        res = s[0]
        for i in range(length - 1):
            odd = centers(s,i,i)
            even = centers(s,i,i+1)
            maxstr = odd if len(odd) > len(even) else even
            if len(maxstr) > maxlen:
                maxlen = len(maxstr)
                res = maxstr
        return res


def centers(strs: str, left:int,right:int):
    length = len(strs)
    i = left
    j = right
    while i >=0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i+1:j]

if __name__ == '__main__':
    j = Solution()
    a = j.longestPalindrome("babad")
    print(a)