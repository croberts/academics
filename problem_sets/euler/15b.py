"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import pprint
pp = pprint.PrettyPrinter(indent=4)


class Node:
    data = {}

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def data(self):
        print(self.left, self.right, self.up, self.down)

    def loc(self):
        print(self.row, self.column)

    def fill(self, left_node, right_node, up_node, down_node):
        self.left = left_node
        self.right = right_node
        self.up = up_node
        self.down = down_node


class Grid:
    def __init__(self, size):
        self.data = []
        self.size = size

        for row in range(0, size + 1):
            self.data.append([])
            for column in range(0, size + 1):
                self.data[row].append(Node(row, column))

    def data(self):
        return self.data

    def root(self):
        return self.data[0][0]

    def end(self):
        return self.data[self.size - 1][self.size - 1]

    def fill(self):
        for row in range(0, self.size + 1):
            for column in range(0, self.size + 1):
                left = self.nested_get(row, column - 1)
                right = self.nested_get(row, column + 1)
                up = self.nested_get(row - 1, column)
                down = self.nested_get(row + 1, column)
                node = self.data[row][column]
                node.fill(left, right, up, down)
        return

    def display(self):
        for row in range(0, self.size + 1):
            for column in range(0, self.size + 1):
                node = self.data[row][column]
                node.data()
                node.loc()

    def nested_get(self, row, column):
        if row > self.size or row < 0 or column > self.size or column < 0:
            return None
        else:
            return self.data[row][column]

    def num_paths(self):
        paths = self.traverse(self.root(), 0)
        return paths

    def traverse(self, current_node, total):
        current_node.loc()

        if(current_node.right):
            self.traverse(current_node.right, total)
        elif(current_node.down):
            self.traverse(current_node.down, total)

        if(current_node == self.end()):
            total = total + 1


def example():
    grid = Grid(2)
    grid.fill()
    # grid.display()
    print("Num paths:", grid.num_paths())

def solution():
    grid = Grid(20)
    grid.fill()
    print(grid.num_paths())

example()


