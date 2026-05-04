"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
"""
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if matrix[r-1][c-1] == "1":
                    top = dp[r-1][c]
                    left = dp[r][c-1]
                    dig = dp[r-1][c-1]
                    dp[r][c] = min(top, left, dig) + 1
                    max_side = max(max_side, dp[r][c])
        return max_side * max_side
