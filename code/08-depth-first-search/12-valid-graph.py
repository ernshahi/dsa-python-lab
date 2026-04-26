"""
DESCRIPTION (inspired by Lintcode.com)
You are given an integer n and a list of undirected edges where each entry in the list is a pair of integers representing an edge between nodes 0 and n - 1. You have to write a function to check whether these edges make up a valid tree.

There will be no duplicate edges in the edges list. (i.e. [0, 1] and [1, 0] will not appear together in the list).

Input: 
n = 4 
edges = [[0, 1], [2, 3]]
Output: False
"""
from collections import defaultdict
from typing import List

class Solution:
    def graph_valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        ad_list = defaultdict(list)
        for x, y in edges:
            ad_list[x].append(y)
            ad_list[y].append(x)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in ad_list[node]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True
        return True if dfs(0, -1) and n == len(visited) else False

# 0 -> 1 -> 2
        
