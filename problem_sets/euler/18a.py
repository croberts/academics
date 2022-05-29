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
"""
"""
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
    Also note: children are shared between nodes. Standard binary tree algos
    will not work.
"""


class Node:
    value = None
    left = None
    right = None

    def __init__(self, data):
        self.value = data

    def display(self):
        print("Value", self.value)
        print("Left", self.left)
        print("Right", self.right)
        print('\n')


class BinaryTree:
    def __init__(self, input_string):
        nums = input_string.replace('\n', '').split(' ')
        nums = [num for num in nums if num is not '']
        nodes = [Node(num) for num in nums]
        for i in range(0, len(nums) - 2):
            node = nodes[i]
            node.left = nums[2*i + 1]
            node.right = nums[2*i + 2]
            node.display()

    def traverse(self):
        pass

    def max_sum(self):
        return None

tree = BinaryTree(input_string)
max_sum = tree.max_sum()
print(max_sum)



