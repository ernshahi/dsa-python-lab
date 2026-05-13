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
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS from all 0s, and update the distance of the nearest 0 for each cell.
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not mat: return mat
        rows, cols = len(mat), len(mat[0])
        result = [ [-1] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    result[r][c] = 0

        distance = 1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<rows and 0<=ny<cols and result[nx][ny] == -1:
                        result[nx][ny] = distance
                        queue.append((nx, ny))
            distance += 1  
        return result


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS from all 1s, and update the distance of the nearest 0 for each cell.
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not mat: return mat
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        distance = 1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for x, y in directions:
                    nx, ny = x + r, y + c
                    if 0<=nx<rows and 0<=ny<cols and (nx, ny) not in visited:
                        mat[nx][ny] = distance
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            distance += 1
        return mat
    
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
