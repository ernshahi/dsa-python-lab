# Backtracking
Backtracking = DFS + Pruning
DFS is the traversal. Backtracking is DFS + decision-making.

- Pruning: Is the optimization to stop the backtracking early.
- Branching: Is the number of choices we have at each step.
- Backtracking: Is the process of removing the last choice and trying the next choice.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        rows, cols = len(board), len(board[0])

        def backtrack(i, j, idx):
            if len(word) == idx:
                return True
            if i < 0 or i >=rows or j < 0 or j >=cols or board[i][j] != word[idx]:
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