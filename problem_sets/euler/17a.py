"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage.
"""
single = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]
teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

single_counts = sum([len(x) for x in single])
teens_counts = sum([len(x) for x in teens])
tens_counts = sum([len(x) for x in tens])

hundred_count = 7
thousand_count = 8
and_count = 3


# 1 to 99 inclusive.
def ninety_nine():
    # 1 - 9  * 9 (no teens, otherwise ten)
    first_digit_total = single_counts * 9

    # 11 - 19
    teens_total = teens_counts

    # twenty-ninety * 10 uses per bucket
    third_digit_total = (tens_counts * 10)

    return first_digit_total + teens_total + third_digit_total


def one_thousand():
    """
    01-99
    (1)01-99
    ...etc == 99 * 10
    """
    first_and_second_digit_total = ninety_nine() * 10

    """
    one hundred
    one hundred and (one)
    ...
    one hundred and (ninety nine)
    == "one hundred" * 100
    """
    first_word = single_counts * 100
    second_word = hundred_count * 899
    third_word = and_count * 899
    third_digit_total = first_word + second_word + third_word

    fourth_digit_total = 3 + thousand_count

    return first_and_second_digit_total + third_digit_total + fourth_digit_total

print(one_thousand())
