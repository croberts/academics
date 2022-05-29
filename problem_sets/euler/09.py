from math import sqrt

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
c = sqrt(a^2 + b^2)
"""


def pythag_trip():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = sqrt(pow(a, 2) + pow(b, 2))
            if a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)


pythag_trip()
