"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the
 greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


"""

"""
Plan A: Brute force

1. For each number 1 to 28123, 
    a. find the proper divisors,
    b. sum,
    c. categorize (abundant, def, perf).
    d. if abundant, add to abundant_numbers list.

out -> list of all abundant numbers

2. for each number in abundant_numbers:
    a. sum with every number after it in the list.
        I. with each a + b sum, add that number to a set.

out -> list of all a + b sums of abundant numbers -> abundant_number_sums

3. for each integer 1 to 28123,
    a. if the number is not in abundant_number_sums, sum to running total.

return running total.
"""