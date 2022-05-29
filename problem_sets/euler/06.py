"""The sum of the squares of the first ten natural numbers is
1^2 + 262 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""
from math import pow


def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + pow(i, 2)
    return sum


def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return pow(sum, 2)


def foo():
    su_sq = sum_of_squares(100)
    sq_su = square_of_sum(100)
    print(su_sq)
    print(sq_su)
    return sq_su - su_sq

print(foo())
