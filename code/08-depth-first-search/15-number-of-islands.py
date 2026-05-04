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
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def _helper(r, c):
            grid[r][c] = "0"
            for x, y in directions:
                nx, ny = r + x, c + y
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == "1":
                    _helper(nx,ny)
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    result += 1
                    _helper(r, c)
        return result
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    result += 1
                    dfs(r, c)
        return result

                            
# Bonus: replace grid itself to save space

if __name__ == "__main__":
    inputs = [["1"]]
    print(Solution().numIslands(inputs))
    