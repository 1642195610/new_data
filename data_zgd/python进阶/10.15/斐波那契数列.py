import time


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

start= time.time()

print(fib(40))
end = time.time()
dur = end - start
print(dur)


# def pow(n):
#     a = np.array([[1, 0], [0, 1]])
#     b = np.array([[1, 1], [1, 0]])
#     n -= 1
#     while (n > 0):
#         if (n % 2 == 1):
#             a = np.dot(b, a)
#         b = np.dot(b, b)
#         n >>= 1
#     return a[0][0]
#
#
# n = int(input())
# print(factorial(n))