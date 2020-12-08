""" 
    Mike Zhong
    Homework 6
    CS566 Analysis of Algorithms
    Due: 4/19/17

    Can be run from the command line:
    $ python hw6.py --problem --number_of_items --max_item_weight --max_item_value --max_knapsack_weight
    By default, the number of items will be 10 with a max weight and max value of 100, the knapsack has a max
    default weight of 500

    Two methods for the binary knapsack are provided, a top-down naive recursive solution and a memoized bottom-up 
    solution that does not use recursion. For the unbounded knapsack problem, a memoized bottom-up solution is used.
"""

import os
import time
import argparse
import random
import math

parser = argparse.ArgumentParser(usage="Solutions to the 0-1 integer knapsack problem and "
                                       "unbounded integer knapsack problem",
                                 description="Enter argument 1 to use memoized recursion and 0 for naive recursion")

parser.add_argument('problem', default=0, nargs="?", const=1,
                    type=int, help="enter 0 for 0-1 integer knapsack problem, "
                                   "enter 1 for unbounded integer knapsack problem")

parser.add_argument('n', default=10, nargs="?", const=1,
                    type=int, help="enter number of items to be considered for the knapsack problem")

parser.add_argument('max_weight', default=100, nargs="?", const=1,
                    type=int, help="enter the max weight of the knapsack")

parser.add_argument('max_value', default=100, nargs="?", const=1,
                    type=int, help="enter the max value of the items to choose from")

parser.add_argument('sack_weight', default=500, nargs="?", const=1,
                    type=int, help="enter the max weight of the knapsack")

args = parser.parse_args()

if args.problem is 0:
    fp = open(os.getcwd() + "/hw6_output_01.txt", 'a+')
else:
    fp = open(os.getcwd() + "/hw6_output_unbounded.txt", 'a+')


# 0-1 integer knapsack problem
# Naive recursive implementation. Top-down approach. Not Dynamic Programming
def solve_01(n, W, weights, values):
    if n is 0 or W is 0:
        return 0
    if weights[n-1] > W:
        return solve_01(n-1, W, weights, values)
    else:
        return max(values[n-1] + solve_01(n-1, W-weights[n-1], weights, values),
                   solve_01(n-1, W, weights, values))


# 0-1 integer knapsack problem
# Dynamic programming approach using memoization. Bottom-up
def solve_01_dp(n, W, weights, values):
    # initialize table of solutions
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # build the table bottom-up
    for i in range(n+1):
        for w in range(W+1):
            if i is 0 or w is 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w - weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

# unbounded integer knapsack problem
# Dynamic programming approach using memoization. Bottom-up
def solve_unbounded(n, W, weights, values):
    K = [0 for x in range(W+1)]

    for w in range(W+1):
        for i in range(n):
            if weights[i] <= w:
                K[w] = max(K[w], K[w - weights[i]] + values[i])

    return K[W]


# Initialize random item weights and values
# item weights will range from 1 to half the max knapsack weight capacity
# item values will range from 1 to the user defined max item value
random.seed(42)
weights = []
values = []

for i in range(args.n):
    weights.append(random.randint(1, math.floor(args.max_weight/2)))
    values.append(random.randint(1, args.max_value))

fp.write("Initializing random weights and values for items...\n")
fp.write(str(args.n) + " items\n")
fp.write("Weights: " + str(weights) + "\n")
fp.write("Values: " + str(values) + "\n")
fp.write("Max knapsack weight: " + str(args.sack_weight) + "\n")

if args.problem is 0:
    t = 2
    while t is not 0 and t is not 1:
        t = int(raw_input("You have selected the 0-1 integer knapsack problem, use naive approach (0) or memoized approach (1)? (0/1) "))
    if t is 0:
        fp.write("Solving the binary knapsack problem with naive recursion\n")
        now = time.time()
        ans = solve_01(args.n, args.sack_weight, weights, values)
        elapsed = time.time() - now
    elif t is 1:
        fp.write("Solving the binary knapsack problem with memoization\n")
        now = time.time()
        ans = solve_01_dp(args.n, args.sack_weight, weights, values)
        elapsed = time.time() - now

else:
    fp.write("Solving the unbounded knapsack problem with memoization\n")
    now = time.time()
    ans = solve_unbounded(args.n, args.sack_weight, weights, values)
    elapsed = time.time() - now

fp.write("Problem solved! The max value of the knapsack given max weight of " + str(args.sack_weight) + " is...\n")
fp.write(str(ans) + "\n")
fp.write("Time to solve problem: " + str(elapsed) + "\n")




