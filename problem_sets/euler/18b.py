""""
By starting at the top of the triangle below and moving
to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""

input_string = """
                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

"""
    NOTE: As there are only 16384 routes,
    it is possible to solve this problem by trying every route.
    However, Problem 67, is the same challenge with a triangle
    containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)
"""

nums = input_string.split('\n')
rows = [num.strip() for num in nums if num is not '']
num_rows = []

for row in rows:
    num_rows.append(row.split(' '))


def choose_largest(row, column):
    current = num_rows[row][column]
    print(current)

    the_sum = 0

    for index in range(0, len(num_rows)):
        try:
            left = int(num_rows[index + 1][column])
        except IndexError:
            pass

        try:
            right = int(num_rows[index + 1][column + 1])
        except IndexError:
            pass

        if left > right:
            the_sum = the_sum + left
            print(left)
        else:
            the_sum = the_sum + right
            column = column + 1
            print(right)

    return the_sum

ans = choose_largest(0, 0)
print("Sum: ", ans)

"""
    Insight: I think we want something like the mode of indexes of maximums.
    By that I mean, we create tuples (index, value)
    and order by value, of each row.
    Then we try to find the path with the min distance.
    I'm not 100% sure this will yield a different algo.
    There is probably a tweak here somewhere.
    Let me try my prev. algo from the bottom, via max.
    Not entirely aware of everything.

    Hmm, no. two are the same.
    I think we should calc first five top rows, max that.
    The top rows have less influence
    in terms of value because they are common to far more rows. five or height/2.
"""

def choose_largest2(row, column):
    current = num_rows[row][column]
    print(current)

    the_sum = 0

    for index in range(len(num_rows), 0, -1):
        try:
            left = int(num_rows[index - 1][column - 1])
        except IndexError:
            pass

        try:
            right = int(num_rows[index - 1][column])
        except IndexError:
            pass

        if left > right:
            the_sum = the_sum + left
            print(left)
        else:
            the_sum = the_sum + right
            column = column + 1
            print(right)

    return the_sum


def get_top_half(num_rows):
    end = len(num_rows + 1)
    top_nums = []

    for index, item in num_rows[end]:
        if item > max_num:
            max_num = item
            max_index = index


