""" 
    Mike Zhong
    Homework 7
    CS566 Analysis of Algorithms
    Due: 5/1/17

    Can be run from the command line:
    $ python hw7.py
    
    This script will use Prim's algorithm to find the MST for the graph given in 23.1 of the textbook.
    The function call provides the Graph in the form of an adjacency matrix, with INF in the diagonals and entries
    where connections do not exist. The algorithm is greedy in that it takes the minimum weighted edge at
    each iteration and adds the connected node to its tree. This is a locally optimal decision which does not take into 
    account other connections away from the given node.
    
    The output is a set of connections that form the MST, as well as their associated weights.
    The sum cost of the MST is also written to file.
    
    The script can be run with with any non-directional weighted graph but you must provide the input as a numpy array
    and ensure the adjacency matrix is valid.
"""

import numpy as np
inf = float('inf')


def min_key(key, mst_set, num_vertices):
    """
    Given the current key table and the current mst_set, will return the index of the adjacent node of minimum weight
    :param key: key table
    :param mst_set: The current set of nodes making up the MST tree
    :param num_vertices: number of nodes in the original tree
    :return: index of the node with minimum weight connection to some parent[index] node
    """
    min = inf

    # iterate over the nodes
    for i in range(num_vertices):
        # if the node is not already in the mst_tree and it has a valid weight less than the current minimum weight
        if mst_set[i] is False and key[i] < min:
            # remember the weight and index
            min = key[i]
            min_idx = i

    return min_idx


def prims(A):
    """
    Prim's algorithm for finding the Minimum Spanning Tree
    :param A: The adjacency matrix of a given graph, must be valid, is not checked here
    :return: A list where the index and value are the node connections forming the MST
    """
    num_vertices = A.shape[0]
    key = [inf]*num_vertices  # stores the node with minimum weight to current node
    parent = [None]*num_vertices  # stores the parent node that the index node has minimum weight to
    mst_set = [False]*num_vertices  # indicates whether a node has been added to our tree

    # start at node 0
    key[0] = 0

    for _ in range(num_vertices):
        # start at node 0, include it in our MST set
        i = min_key(key, mst_set, num_vertices)
        print "i: ", i
        print "parent[i]: ", parent[i]
        mst_set[i] = True

        # iterate over all nodes
        for j in range(num_vertices):

            # if there is a connection and weight between node i and j,
            # and node j is not already in our tree
            # and the weight is less than the existing key for node j
            if (A[i][j] is not inf) and (mst_set[j] is False) and (A[i][j] < key[j]):
                # update key and parent entries for node j
                # node j now has a key which is the weight, and a parent
                parent[j] = i
                key[j] = A[i][j]

    return parent

# The graph in 23.1 has the following adjacency matrix as numpy array
A = np.array([
     [inf, 4, inf, inf, inf, inf, inf, 8, inf],  # a
     [4, inf, 8, inf, inf, inf, inf, 11, inf],  # b
     [inf, 8, inf, 7, inf, 4, inf, inf, 2],  # c
     [inf, inf, 7, inf, 9, 14, inf, inf, inf],  # d
     [inf, inf, inf, 9, inf, 10, inf, inf, inf],  # e
     [inf, inf, 4, 14, 10, inf, 2, inf, inf],  # f
     [inf, inf, inf, inf, inf, 2, inf, 1, 6],  # g
     [8, 11, inf, inf, inf, inf, 1, inf, 7],  # h
     [inf, inf, 2, inf, inf, inf, 6, 7, inf]  # i
    ])

vertex_map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# This function will take any valid adjacency matrix passed as an argument to the prims() function
# and return the MST
tree = prims(A)
cost = 0
with open("hw7_output.txt", 'w') as fp:
    for i in range(len(tree)):
        if tree[i] is not None:
            cost += A[i][tree[i]]
            fp.write("Vertex " + str(vertex_map[tree[i]]) + " is connected to vertex " + str(vertex_map[i]))
            fp.write("\nTheir weight is " + str(A[i][tree[i]]) + "\n")

    fp.write("\nThe total cost of the MST is: " + str(cost))


