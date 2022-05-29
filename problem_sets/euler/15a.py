"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""


def node():
    tree = {}
    tree['left'] = None
    tree['right'] = None
    return tree


def build(tree, size):
    if size > 1:
        tree['left'] = node()
        tree['right'] = node()
        build(tree['left'], size - 1)
        build(tree['right'], size - 1)
    return tree


"""
q = build(node(), 2)
print(q)

The above is a bad implementation of this type of grid.
Why?
    -> Nodes in a grid have multiple parents, in this case, two parents.
    -> The tree isn't balanced.

Let's start again.
"""
