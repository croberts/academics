"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?"""

min_int = 2520
max_int = 1689515283456000
the_range = [7, 9, 11, 13, 16, 17, 18, 19, 20]


def is_special_div(n):
    for i in the_range:
        if n % i is not 0:
            return False
    return True


def find_smallest_special_div():
    for i in range(min_int, max_int):
        if is_special_div(i):
            return i

n = find_smallest_special_div()
print(n)

""" To get the numbers in the_range to lower the search space, use:
def low_primes():
    for i in range(1, 21):
        if is_prime(i):
            print(i)
"""
