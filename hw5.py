""" Mike Zhong
    Homework 5
    CS566 Analysis of Algorithms
    Due: 4/10/17

    Can be run from the command line:
    $ python hw5.py --dp

    Enter 0 to use naive recursion and 1 to use memoized recursion. For naive, the first 40 numbers are computed
    and their run times recorded. For the memoized recursion, the first 1000 numbers are computed and their run
    times recorded.
"""

import os
import time
import argparse

parser = argparse.ArgumentParser(usage="Compute Fibonacci sequence using naive recursion or memoized recursion",
                                 description="Enter argument 1 to use memoized recursion and 0 for naive recursion")

parser.add_argument('dp', default=0, nargs="?", const=1,
                    type=int, help="enter 1 to use memoization, 0 to use naive recursion")

args = parser.parse_args()

if args.dp is 0:
    fp = open(os.getcwd() + "/hw5_output_fib.txt", 'w')
else:
    fp = open(os.getcwd() + "/hw5_output_fib_dp.txt", 'w')

# a) Traditional recursive algorithm for finding the nth Fibonacci number
def fib(n):
    """Returns the nth term in the Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# b) top-down dynamic programming algorithm for the same problem
memo = {}
def fib_dp(n):
    """Returns the nth term in the Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in memo:
            memo[n] = fib_dp(n-1) + fib_dp(n-2)
        return memo[n]


i = 0
# Use regular recursive fib() to compute fibonacci sequence, time each run
if args.dp is 0:
    print "Running naive recursion for first 40 fibonacci numbers... see hw5_output_fib.txt for results"
    while i < 40:
        s = time.time()
        fp.write(str(i) + " fibonacci number: " + str(fib(i)) + "\n")
        fp.write("run time: " + str(time.time() - s) + " seconds\n")
        i += 1
        print i
# Use dynamic programming and memoized recursion to compute fibonacci sequence, time each run
else:
    print "Running memoized recursion for first 1000 fibonacci numbers... see hw5_output_fib_dp.txt for results"
    while i < 1000:
        s = time.time()
        fp.write(str(i) + " fibonacci number: " + str(fib_dp(i)) + "\n")
        fp.write("run time: " + str(time.time() - s) + " seconds\n")
        i += 1
        memo = {}
        print i

fp.close()




