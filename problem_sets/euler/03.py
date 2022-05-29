"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def is_factor(a, n):
    return n % a == 0


def largest_prime_factor(n):
    sqfac = math.ceil(math.sqrt(n))
    for i in range(sqfac, 0, -1):
        if is_factor(i, n):
            print("%s is factor" % i)
        if is_prime(i):
            print("%s is prime" % i)
        if is_factor(i, n) and is_prime(i):
            return i
    return 0

lpf = largest_prime_factor(600851475143)
print(lpf)
