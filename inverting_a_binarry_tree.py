"""
Inverting a binary tree
"""

from binarytree import build
from binarytree import tree

# recursive way
def invert_binary_tree(ftree):
    if ftree:
        # THIS DOES NOT WORK. Intial ftree.left is lost at first assignment.
        # ftree.left = invert_binary_tree(ftree.right)
        # ftree.right = invert_binary_tree(ftree.left)

        # Multiple assignments work perfectly!
        ftree.left, ftree.right = invert_binary_tree(ftree.right), invert_binary_tree(ftree.left)
    return ftree


if __name__ == "__main__":
    nodes = [1, 6, 4, 8, 1, 3, 6, 9, 5, 4, 2, 3, 6, 8, 9]
    tree = build(nodes)
    print("tree: ", tree)

    print("tree.value returns: ", tree.value)
    print("tree.left returns: ", tree.left)
    print("tree.right returns: ", tree.right)
    print("tree.right.value returns: ", tree.right.value)


    print("original tree: ", tree)
    print("inverted tree: ", invert_binary_tree(tree))

