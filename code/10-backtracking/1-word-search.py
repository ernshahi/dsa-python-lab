"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >=rows or j < 0 or j >= cols or board[i][j] != word[idx]:
                return False
            idx += 1
            temp = board[i][j]
            board[i][j] = "#"
            found = (
                backtrack(i+1, j, idx) or
                backtrack(i-1, j, idx) or
                backtrack(i, j+1, idx) or
                backtrack(i, j-1, idx)
            )
            board[i][j] = temp
            return found
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False