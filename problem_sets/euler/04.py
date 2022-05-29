"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

import math


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest_palindrome_algo_a():
    for n in range(999, 99, -1):
        for m in range(999, 99, -1):
            if is_palindrome(n * m):
                print(n, m, n * m)
                return n * m


def largest_palindrome_algo_b():
    for n, m in zip(range(999, 99, -1), range(999, 99, -1)):
        if is_palindrome(n * m):
            print(n, m, n * m)
            return


def largest_palindrome_algo_c():
    for n in range(998001, 9801, -1):
        if is_palindrome(n) and math.floor(math.sqrt(n)) == math.sqrt(n):
            print(math.sqrt(n), n)
            return


def largest_palindrome_algo_d():
    for n in range(998001, 9801, -1):
        if is_palindrome(n):
            print(n)
            return


def largest_palindrome_algo_e():
    for n in range(998001, 10000, -1):
        if is_palindrome(n):
            for m in range(836, 999):
                if is_factor_below(m, n):
                    print(m)
                    print(n / m)
                    print(n)
                    return


def is_factor_below(a, n):
    return n % a == 0 and n / a < 1000


largest_palindrome_algo_e()
