class Solution:
    def find_gongyueshu(self, a, b):
        if a > b:
            min = b
        else:
            min = a
        for i in range(1, min + 1):
            if (a % i == 0) and (b % i == 0):
                c = i
        return c


if __name__ == '__main__':
    a = 88
    b = 24
    s = Solution()
    result = s.find_gongyueshu(a, b)
    print(result)