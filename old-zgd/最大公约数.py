def get_greatest_common_divisor(a,b):
    big = max(a,b)
    small = min(a,b)
    if big % small == 0:
        return small
    for i in range(small // 2,1,-1):
        if big % i == 0 and small % i == 0:
            return i

# 辗转相除法
def get_greatest_common_divisor_1(a,b):
    big = max(a,b)
    small = min(a,b)
    if big % small == 0:
        return small
    return get_greatest_common_divisor_1(big % small,small)

# 更相减损术
def get_greatest_common_divisor_2(a,b):
    if a - b == 0:
        return a
    big = max(a,b)
    small = min(a,b)
    return get_greatest_common_divisor_2(big - small,small)

if __name__ == '__main__':
    print(get_greatest_common_divisor(10,50))
    print(get_greatest_common_divisor_1(10,50))
    print(get_greatest_common_divisor_2(10,50))

