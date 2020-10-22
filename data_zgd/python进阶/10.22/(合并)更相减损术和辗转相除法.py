def greatest_common_divisor(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    mod = a % b
    result = b
    if mod == 0:
        result = b
    else:
        if not (a & 1) and not (b & 1):
            result = greatest_common_divisor(a >> 1, b >> 1) << 1
        elif not (a & 1) and b & 1:
            result = greatest_common_divisor(a >> 1, b)
        elif a & 1 and not b & 1:
            result = greatest_common_divisor(a, b >> 1)
        elif a & 1 and b & 1:
            result = greatest_common_divisor(b, a - b)
    return result


if __name__ == '__main__':
    a = 88
    b = 24
    result = greatest_common_divisor(a, b)
    print(result)
