"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        def helper():
            stacks = []
            visited.add((i, j))
            stacks.append((i, j))
            
            while stacks:
                a, b = stacks.pop()
                for x, y in directions:
                    if 0 <=x + a < rows and 0 <= y + b < cols:
                        if (x+a, y+b) not in visited and grid[x+a][y+b] == "1":
                            stacks.append((x+a, y+b))
                            visited.add((x+a, y+b))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0" or (i, j) in visited:
                    continue
                result += 1
                helper()
        return result

                            
# Bonus: replace grid itself to save space

if __name__ == "__main__":
    inputs = [["1"]]
    print(Solution().numIslands(inputs))