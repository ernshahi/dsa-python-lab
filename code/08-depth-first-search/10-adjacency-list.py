"""
DESCRIPTION
Given an integer n which represents the number of nodes in a graph, and a list of edges edges, where edges[i] = [ui, vi] represents a bidirectional edge between nodes ui and vi, write a function to return the adjacency list representation of the graph as a dictionary. The keys of the dictionary should be the nodes, and the values should be a list of the nodes each node is connected to.

Example:
n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
"""
from collections import defaultdict

def build_adjacency_list(n, edges):
    result = defaultdict(list)
    for x, y in edges:
        result[x].append(y)    
        result[y].append(x)
    return result

if __name__ == "__main__":
    n = 4
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
    print(build_adjacency_list(n, edges))
    
    