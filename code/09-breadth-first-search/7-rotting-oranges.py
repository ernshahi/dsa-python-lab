"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: 
            return -1
        
        rows, cols = len(grid), len(grid[0])
        rotten_oranges = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        # no need to visited set as we are modifying the grid in place
        time = 0
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while rotten_oranges and fresh_count > 0:
            time += 1
            length = len(rotten_oranges)
            for _ in range(length):
                x, y = rotten_oranges.popleft()
                for rd, cd in directions:
                    rn, cn = rd + x, cd + y
                    if 0<=rn<rows and 0<=cn<cols and grid[rn][cn] == 1:
                        grid[rn][cn] = 2
                        rotten_oranges.append((rn, cn))
                        fresh_count -= 1
        return time if fresh_count == 0 else -1