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

"""
    self notes:
    0
    1
    3
    6
    10
    15
    21

    --
    0
    2
    5
    9
    14
"""


# NOTE: done.
def compact(a_list):
    return [int(x) for x in a_list if x is not None]


# NOTE: done.
def get_adj_lists(triangle_nums):
    adj_lists = []
    for row_index in range(0, len(triangle_nums)):
        row = triangle_nums[row_index]
        try:
            next_row = triangle_nums[row_index + 1]
        except IndexError:
            next_row = None

        if next_row:
            for column_index in range(0, len(row)):
                item = row[column_index]
                item_south = next_row[column_index]
                try:
                    item_southeast = next_row[column_index + 1]
                except IndexError:
                    item_southeast = None

                adj_list = [item, item_south, item_southeast]
                adj_lists.append(compact(adj_list))
    return adj_lists

"""
def sum_stuff(adj_lists, row_index, column_index, running_total_south, counter):
    counter = counter + 1
    row = adj_lists[row_index]
    running_total_south = running_total_south + sum_south(row, column_index)

    # running_total_southeast = sum_southeast(row, column_index)

    try:
        next_row = adj_lists[row_index + 1]
    except IndexError:
        next_row = None

    if next_row:
        sum_stuff(adj_lists, row_index + counter, 0, running_total_south, counter)

    return running_total_south


def sum_south(row, column_index):
    item = row[column_index]
    item_south = row[column_index + 1]
    return int(item) + int(item_south)


def sum_southeast(row, column_index):
    item = row[column_index]
    item_south = row[column_index + 2]
    return int(item) + int(item_south)

"""


def get_left_path(adj_lists, path, row_pointer):
    root = adj_lists[0]
    root_value = root[0]
    path.append(root_value)

    adj_lists = adj_lists[row_pointer:]
    row_pointer = row_pointer + 1

    if adj_lists:
        get_left_path(adj_lists, path, row_pointer)
    else:
        return path.append(root[1])


def get_right_path(adj_lists, path, row_pointer):
    root = adj_lists[0]
    root_value = root[0]
    path.append(root_value)

    adj_lists = adj_lists[row_pointer:]
    row_pointer = row_pointer + 1

    if adj_lists:
        get_right_path(adj_lists, path, row_pointer)
    else:
        return path.append(root[2])


nums = input_string.split('\n')
triangle_nums = [num.strip().split(' ') for num in nums if num is not '']

# Build adjacency list
adj_lists = get_adj_lists(triangle_nums)
print(adj_lists)

path = []
get_left_path(adj_lists, path, 1)

#get_right_path(adj_lists, path, 2)
print(path)
print(sum(path))
"""
ttl = sum_stuff(adj_lists, 0, 0, 0, 0)
print(ttl)
"""
