""""
By starting at the top of the triangle below and moving
to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.


Find the maximum total from top to bottom of the triangle below.

    NOTE: As there are only 16384 routes,
    it is possible to solve this problem by trying every route.
    However, Problem 67, is the same challenge with a triangle
    containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)
"""
from math import factorial


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
Plan A: Brute force
1. Build a tree. Duplicate adjacent values. E.g. in the tree:
        75
        95 64
        17 47 82

47 is the child of both 95 and 64. 

2. After the complete tree is generated, calculate every path. Store the running max. 
Use a tree algo: depth-first search.

Plan B: Use a graph instead of duplicating values. Use a* or something, searching for the maximum
- Assumption: earlier optimizations will achieve the best outcomes. This may prove fatal.

Plan C: Use maximin with alpha-beta pruning
- Assumption: same as above

Plan D: Caching
- Cache earlier routes as there is less combinatorially, and we don't care about the individual numbers beyond the sum. E.g.: 
                   75
                 95 64
                17 47 82

75 + 95 = 170
75 + 64 = 139

This collapses the tree to:

  170 139
 17  47  82

So instead of calculating:

75 + 95 + 17, 75 + 95 + 47, 75 + 64 + 47, 75 + 64 + 82 (8 traversals)
we do
75 + 95 = 170, 75 + 64 = 139, 170 + 17, 170 + 47, 139 + 47, 139 + 82 (6 traversals)

This is more of a breadth-first approach. 

Pros:
- Probably not much in memory
- No need to duplicate data and then iterate



Discovery 1:
Some paths are functionally the same.
-> no. The answer is, when two paths collide on the same node,
you can evaluate immediately which is the better path previous to that point,
because all subsequent nodes can be equal.

so where to compare?

Discovery 2:
Can we just do some sort of adjacent sliding window?

            19 01 23 75 03 34
            a  b  c  d  e  f
            
            a  bc 

max(a, b)
max(b, c)

max() all the ones in the middle. but don't chain maxes together.

"""

# Approach: Plan D
nums = input_string.replace('\n', '').split(' ')
triangle = [int(num) for num in nums if num != '']


def get_index(cur, row, i):
    if row == 1:
        return 0
    if row == 2:
        return 1
    else:
        if cur < row:
            cur = cur + 1


def get_row(n):
    #1 2 3 4 5 6 7
    #0 1 3 6 10 15 21

    # they are triangular numbers!

    # ( n+1 ) 
    # (  2  )
    # -> 
    # (n + 1)! / (2! * (n+1-2)!)

    if n == 0:
        return [triangle[0]]

    index = int(factorial(n + 1) / ( factorial(2) * factorial(n -1) ))
    #print(index)
    return triangle[index: index + n + 1]


def print_triangle(num_rows):
    for i in range (0, num_rows):
        print(get_row(i))


def optimize_rows(num_rows):
    current_row = get_row(0)

    for i in range (1, num_rows):
        new_row = []

        print('\n')
        print("current row: ", current_row)

        next_row = get_row(i)
        print("next row: ", next_row)


        for index, value in enumerate(current_row):
            #print(index, value)
            #print(len(current_row))
            new_row.append(value + next_row[index])

            if index != len(next_row) - 1:
                new_row.append(value + next_row[index + 1])
        print("new row:", new_row)

        #current_row = new_row
        
        final_row = [new_row[0]]

        index = 1
        while index < len(new_row) - 1:
            if index < len(new_row) - 2:
                #print(new_row[index], new_row[index + 1])
                final_row.append(
                    max(new_row[index], new_row[index + 1])
                )
                index = index + 2
        
        final_row.append(new_row[-1])
        print("final row: ", final_row)

        current_row = final_row

    return current_row
   
last_row = optimize_rows(15)
print(max(last_row))
#print_triangle(15)

"""
[170, 139]
[17, 47, 82]
[187, 217, 186, 221]
max(217, 186)= 217

[187, 217, 221]

[18 35 87 10] 

[205, 222, 252, 304, 308, 231]
0
1,2
2,3
3,4
5
[20, 4, 82, 47, 65]

"""

