"""
Given a reference to a variable node which is part of an undirected, connected graph, write a function to return a copy of the graph as an adjacency list in dictionary form. The keys of the adjacency list are the values of the nodes, and the values are the neighbors of the nodes.

node is an instance of the following class, where neighbors is a list of references to other nodes in the graph (also of type IntGraphNode):


Example:
node = IntGraphNode(1, [IntGraphNode(2), IntGraphNode(3)])
output: {1: [2, 3], 2: [1], 3: [1]}
"""

from typing import Dict, List

class IntGraphNode:
    def __init__(self, value, id, neighbors):
        self.value = value
        self.id = id
        self.neighbors = neighbors

class Solution:
    def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:
        new_graph = {}
        def clone(node):
            if node.value in new_graph:
                return
            new_graph[node.value] = [n.value for n in node.neighbors]
            for neighbor in node.neighbors:
                clone(neighbor)
        if node:
            clone(node)
        return new_graph
