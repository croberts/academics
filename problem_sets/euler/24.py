"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?
"""

"""
Plan A: BF

1. Treat "0123456789" as a string.
2. Generate all permutations.
3. Convert all permutations.
4. Sort all permutations.
5. Grab the millionth.

Op 1:
0 123 456 789
Given the number of digits, this # is essentially a billion.
Hmm, that won't work.

Op 2:


"""
from itertools import permutations
import itertools



s = "0123456789"

x = list(itertools.permutations(s))

vals = []

for y in x:
    y = ''.join(y)
    #y = int(y)
    vals.append(y)

vals.sort()

print(len(vals))
print(vals[1000000 - 1])