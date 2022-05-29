"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(end):
    x = 1
    for i in range(0, end):
        x = x + 1
        while(not is_prime(x)):
            x = x + 1
    return x

print(is_prime(9))

for i in range(1, 7):
    print(find_prime(i))

print(find_prime(10001))
