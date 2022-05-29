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
    'zero',
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
    'ten',
    'tweens',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]

"""Let's try it the visual, debugging way."""

numbers = []
hundred = "hundred"

def get_single(i):
    if i == 0:
        return ""
    else:
        return single[i]

def get_word(i):
    if i < 10:
        return get_single(i)
    elif i == 10:
       return tens[0]
    elif i < 20:
        return teens[i % 10]
    elif i < 100:
        return tens[i//10] + get_single(i%10)
    elif i < 1000:
        lhs = get_single(i//100) + hundred
        if i % 100 != 0:
            lhs = lhs + "and"
        rhs = get_word(i%100)
        return lhs + rhs
    else:
        return "onethousand"

def get_word_info(n):
    word = get_word(n)
    return (n, word, len(word))


def show(end):
    word_total = 0
    for i in range(1, end): 
        word_info = get_word_info(i)
        print(word_info)
        word_total = word_total + word_info[2]
    print(word_total)

show(6)
show(1001)

"""
Lessons learned:

- Printing debugging statements is still useful, even when the task seems trivial.
- Organizing and solving the project logically and in a clearly readable manner is 
far more useful to debug errors, than is pre-optimizing the solution and attempting to 
debug the issue from there.

"""
