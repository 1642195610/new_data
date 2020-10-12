# import time
#
#
# start = time.time()
# def fib(n):
#     if n <=2:
#         return 1
#     return fib(n-1) + fib(n-2)
# result = fib(4)
# end = time.time()
# print(end - start)
# print(result)

import time


start = time.time()


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


result = fib(4)
end = time.time()
print(end - start)
print(result)
