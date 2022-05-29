"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
from math import pow


def sum_digits(num):
    num_string = str(num)

    running_total = 0

    for char in num_string:
        running_total = running_total + int(char)

    return running_total


example = sum_digits(int(pow(2, 15)))
print(example)

result = sum_digits(int(pow(2, 1000)))
print(result)
