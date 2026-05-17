"""
289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 -> 0 -> 0
        1 -> 0 -> 1
        0 -> 1 -> 2
        1 -> 1 -> 3
        """
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, 0), (1, 0),
            (-1, 1), (1, -1),
            (0, 1), (0, -1),
            (1, 1), (-1, -1),
            ]
        def count_nei(r, c):
            alive_count = 0
            for dx, dy in directions:
                nx, ny = dx + r, dy + c
                if not (0 <= nx < rows and 0<=ny<cols):
                    continue
                if board[nx][ny] in [1, 3]:
                    alive_count += 1
            return alive_count
        
        # def count_nei1(r, c):
        #     for i in range(r-1, r+2):
        #         for j in range(c-1, c+2):
        #             if (i==r and j==c):
        #                 continue
        #             if i<0 or j<0 or i>=rows or j>=cols:
        #                 continue
        #             if board[i][j] in [1, 3]:
        #                 alive_count += 1
        #     return alive_count

        for r in range(rows):
            for c in range(cols):
                alive_count = count_nei(r, c)
                if board[r][c] == 1:
                    if alive_count in [2, 3]:
                        board[r][c] = 3
                else:
                    if alive_count == 3:
                        board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 3:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 1:
                    board[r][c] = 0
                # else 0
        return board
