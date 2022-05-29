import math


def collatz(n):
    k = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        k = k + 1
    return k


def find_longest_collatz():
    one_mil = int(math.pow(10, 6))
    longest_c = 1
    num = 0

    for index in range(1, one_mil):
        c = collatz(index)

        if c > longest_c:
            num = index
            longest_c = c
    return num, longest_c

print(find_longest_collatz())
