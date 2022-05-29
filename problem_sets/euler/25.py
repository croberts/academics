"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2 where F1 = 1 and F2 = 1
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def num_digits(num):
    return len(str(num))


def fib_i(i):
    if i == 1 or i == 2:
        return 1
    else:
        current = 1
        prev = 1
        for index in range(2, i):
            current = prev + current
            prev = current - prev
        return current


def fib_r(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fib_r(i - 1) + fib_r(i - 2)


# for index in range(1, 13):
#     print(fib_r(index))

# for index in range(1, 1000):
#     print(fib_i(index))

ans = ""
index = 0
digit_count = 0

while digit_count < 1000:
    index = index + 1
    ans = fib_i(index)
    digit_count = num_digits(ans)
    print(digit_count)


print(ans)
print(num_digits(ans))
print(index)
