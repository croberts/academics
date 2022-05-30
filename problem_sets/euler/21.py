"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

"""
Assumptions:
Using positive, whole integers

Plan A, brute force:

1. Calculate the sum of proper divisors of every number from 1 to 10,000 and store them in an array.
Runtime: n

2. For each sum, check if it has an amicable match. If it does, sum the indexes of the array (+1) and add them to the running total.
Runtime: n

Total runtime: 2n

Optimization 1:
- Do #2 while doing the initial sum. 
    - This could get hairy, how is this an optimization?

Assumption, question:
If a sum > 10,000, should we investigate if it's an amicable number?

-> Assumption was no. Answer: 40284
-> Let's try yes. Answer: 40284. doesn't seem to make a diff.

Solved!

Debug: I had assumed part of the problem statement was irrelevant (where a != b). Earlier, I had also misread the problem statement.

"""
import math

def get_proper_divisors(x):
    divisors = []

    for i in range(1, math.floor(x/2) + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

def get_divisor_sums():
    divisor_sums = []

    for i in range(0, 10000):
        divisors = get_proper_divisors(i)
        divisor_sums.append(sum(divisors))

    return divisor_sums


def check_amicable_matches(divisor_sums):
    amicable_sum = 0
    amicable_count = 0

    for index, value in enumerate(divisor_sums):
        #print(index, value)
        if len(divisor_sums) >= value: # double check this
            if index == divisor_sums[value] and index != value: # check if list index is that high
                amicable_sum += index
                amicable_count = amicable_count + 1
                print(index, value)
        """
        else:
            amicable_num = sum(get_proper_divisors(value))
            if index == amicable_num:
                amicable_sum += index
                amicable_count = amicable_count + 1
        """

    return amicable_sum, amicable_count


def test_get_divisor_sums():
    test_a = get_proper_divisors(220)
    print(sum(test_a) == 284)

    test_b = get_proper_divisors(284)
    print(sum(test_b) == 220)


def run():
    divisor_sums = get_divisor_sums()
    amicable_sum, amicable_count = check_amicable_matches(divisor_sums)
    print(amicable_sum, amicable_count)


divisor_sums = get_divisor_sums()
print(divisor_sums[3960])

divisors = get_proper_divisors(3960)
print(divisors)

run()
