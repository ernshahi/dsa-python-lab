"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two cells sharing a common edge is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat: return mat
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            count = 0
            visited = set((x, y))
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if mat[r][c] == 0:
                        return count
                    for dx, dy in directions:
                        nx, ny = dx+ r, dy + c
                        if 0<=nx<rows and 0<=ny<cols and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    mat[r][c] = bfs(r, c)
        return mat
