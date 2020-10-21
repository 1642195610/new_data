def factorial(n):
    if n <= 2:
        return n
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    n = 3
    print(factorial(n))


def Jump_the_steps(n):
    if n <= 2:
        return n
    else:
        return Jump_the_steps(n - 1) + Jump_the_steps(n - 2)


if __name__ == '__main__':
    n = 5
    result = Jump_the_steps(n)
    print(result)
