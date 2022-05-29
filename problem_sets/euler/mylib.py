import math


def factorial(num):
    y = num
    for index in range(num - 1, 0, -1):
        y = y * index
    return y


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


