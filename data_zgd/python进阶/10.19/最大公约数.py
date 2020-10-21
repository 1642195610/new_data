# 1.暴力
def greatest_common_divisor1(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    if big % small == 0:
        return small
    for i in range(small // 2, 1, -1):
        if big % i == 0 and small % i == 0:
            return i


result = greatest_common_divisor1(88, 24)
print(result)


# 2.辗转相除法 a>b a%b=c c与b的最大公约数即为a与b的最大公约数
def greatest_common_divisor2(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    if big % small == 0:
        return small
    return greatest_common_divisor2(small, big % small)


result2 = greatest_common_divisor2(88, 24)
print(result2)

# 3.更相减损数 a>b a-b=c c与b的最大公约数即为a与b的最大公约数


def greatest_common_divisor3(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    if big % small == 0:
        return small
    return greatest_common_divisor3(small, big - small)


result3 = greatest_common_divisor3(88, 24)
print(result3)
