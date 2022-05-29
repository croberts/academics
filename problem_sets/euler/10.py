"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
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


def sum_primes(end):
    sum = 0
    for i in range(0, end + 1):
        if is_prime(i):
            sum = sum + i
    return sum

eg = sum_primes(10)
print(eg)

two_mil = int(math.pow(10, 6) * 2)
sol = sum_primes(two_mil)
print(sol)
