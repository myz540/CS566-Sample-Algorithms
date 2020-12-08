""" Mike Zhong
    Homework 4
    CS566 Analysis of Algorithms
    Due: 3/27/17

    Can be run from the command line:
    $ python main.py n i j
    n = # of ints to generate
    i = lower bound of range
    j = upper bound of range
    The script will generate a balanced BST by adding nodes one at a time
    The tree will then be printed in-order
    Two sample inputs were used as stated by the homework (10, 1, 50) and (15, 5, 100)
    Output is printed and attached
"""

import argparse
import random

node_counter = 1


# Nodes that make up the BST
class Node(object):

    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None
        self.size = 1


# insert node into BST with root node root
def insert(root, node):
    if root is None:
        root = node
    else:
        if node.data < root.data:
            if root.left is None:
                root.left = node
                global node_counter
                node_counter += 1
            else:
                insert(root.left, node)
        elif node.data > root.data:
            if root.right is None:
                root.right = node
                global node_counter
                node_counter += 1
            else:
                insert(root.right, node)


# in-order traversal, writes data to output file
def traverse(fp, root):
    if root is not None:
        traverse(fp, root.left)
        fp.write(str(root.data) + "\t")
        traverse(fp, root.right)


# expect 3 arguments for number of values, and lower and upper
parser = argparse.ArgumentParser(usage="Create a balanced BST given number of values and bounds",
                                 description="Enter 3 arguments, number of values (n), and bounds (i) and (j)")

parser.add_argument('n', default=20, type=int, help="Number of elements in your tree")
parser.add_argument('low_bound', default=1, type=int, help="Lower bound of your elements")
parser.add_argument('high_bound', default=100, type=int, help="Upper bound of your elements")
random.seed(0)

# parse args
args = parser.parse_args()

data = []

# make sure there are enough distinct elements in the range
if args.high_bound - args.low_bound < args.n-1:
    print "Not enough distinct elements in range, exiting..."
    exit()

# generate n-sized list of distinct ints between the bounds
for i in range(0, args.n):
    temp = random.randint(args.low_bound, args.high_bound)
    while temp in data:
        temp = random.randint(args.low_bound, args.high_bound)
    data.append(temp)

# sort list of ints
data.sort()

# use central element as root node
root = data[len(data) / 2]
data.remove(root)

# create tree
tree = Node(root)

with open("hw4_output.txt", "a") as fp:
    fp.write("Random (seed(0)) ints generated, tree initialized...\n")
    fp.write("Inserting elements and building tree...\n")
    for i in data:
        temp = Node(i)
        insert(tree, temp)

    fp.write("Tree currently has " + str(node_counter) + " nodes\n")
    fp.write("Traversing tree and printing in-order...\n")
    traverse(fp, tree)
    fp.write("\n\n")





