"""
417. Pacific Atlantic Water Flow

You are given an m x n matrix of non-negative integers representing a grid of land, where rain falls on every cell. Each value in the grid represents the height of that piece of land.

The Pacific Ocean touches the left and top edges of the matrix, while the Atlantic Ocean touches the right and bottom edges. Water can only flow from a cell to its neighboring cells directly north, south, east, or west, but only if the height of the neighboring cell is equal to or lower than the current cell.

Write a function to return a list of grid coordinates (i, j) where water can flow to both the Pacific and Atlantic Oceans. Water can flow from all cells directly adjacent to the ocean into that ocean.

Example 1:

Input:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
Output:
[[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return heights
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable):
            reachable.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in reachable and heights[nr][nc]>=heights[r][c]:
                        dfs(nr, nc, reachable)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols-1, atlantic_reachable)
        
        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows-1, c, atlantic_reachable)
        
        return list(atlantic_reachable & pacific_reachable)