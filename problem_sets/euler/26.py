from decimal import Decimal

"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions
with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains
    the longest recurring cycle in its decimal fraction part.
"""


def longest_recurring_cycle():
    pass


def get_rhs(num, denom):
    num = Decimal(num)
    denom = Decimal(denom)
    frac = Decimal(num/denom)
    rhs = str(frac).split(".")
    if len(rhs) > 1:
        rhs = rhs[1]
    else:
        rhs = rhs[0]
    return rhs


def get_cycle(substr):
    """Use floyd's algo."""

    if len(substr) < 6:
        return ""

    turtle_index = 0
    rabbit_index = 1
    turtle = substr[0]
    rabbit = substr[1]

    print(substr)
    # import pdb; pdb.set_trace()
    # Find the region where a repetition occurs.
    while turtle != rabbit and rabbit_index < len(substr) - 2:
        turtle_index = turtle_index + 1
        turtle = substr[turtle_index]
        rabbit_index = rabbit_index + 2
        rabbit = substr[rabbit_index]

    print(turtle_index, rabbit_index, substr[turtle_index:rabbit_index])

    """
    moo = 0
    turtle_index = 0
    turtle = substr[turtle_index]

    # Find the first occurence of a repetition at `moo`.
    while turtle != rabbit:
        turtle_index = turtle_index + 1
        turtle = substr[turtle_index]
        rabbit_index = rabbit_index + 1
        rabbit = substr[rabbit_index]
        moo = moo + 1

    print(turtle_index, rabbit_index, substr[turtle_index:rabbit_index])

    lamb = 1
    rabbit = substr[turtle_index]

    # Find the length of the shortest repetition, lamb being the end.
    while turtle != rabbit:
        turtle_index = turtle_index + 1
        rabbit = substr[rabbit_index]
        lamb = lamb + 1

    cycle = substr[moo:lamb]
    print(cycle, len(cycle), "----")
   """
    cycle = substr[turtle_index:rabbit_index]
    print("Cycle: ", cycle)
    return cycle

longest_cycle = 0
longest_index = 0


for index in range(1, 1000):
    print(index)
    sub_str = get_rhs(1, index)
    len_cycle = len(get_cycle(sub_str))
    if len_cycle > longest_cycle:
        longest_index = index
        longest_cycle = len_cycle

print(longest_index)
print(longest_cycle)
print(get_cycle(get_rhs(1, longest_index)))


