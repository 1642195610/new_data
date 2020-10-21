class Solution:
    def longestpalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        if length == 1 or s == s[::-1]:
            return s
        max_len, start = 1, 0
        for i in range(1, length):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]


if __name__ == '__main__':
    ss = Solution()
    str1 = "babad"
    result = ss.longestpalindrome(str1)
    print(result)


class Solution:
    def longestpalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        maxlen = 1
        res = s[0]
        for i in range(length - 1):
            odd = self.centerspread(s, i, i)
            even = self.centerspread(s, i, i + 1)
            maxstr = odd if len(odd) > len(even) else even
            if len(maxstr) > maxlen:
                maxlen = len(maxstr)
                res = maxstr
        return res

    def centerspread(self, str: str, left: int, right: int) -> str:
        length = len(str)
        i = left
        j = right
        while i >= 0 and j < length:
            if str[i] == str[j]:
                i -= 1
                j += 1
            else:
                break
        return str[i + 1:j]


if __name__ == '__main__':
    s = Solution()
    str1 = "babad"
    result = s.longestpalindrome(str1)
    print(result)


