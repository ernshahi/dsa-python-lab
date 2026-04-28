"""
You are given a chessboard of infinite size where the coordinates of each cell are defined by integer pairs (x, y). The knight piece moves in an L-shape, either two squares horizontally and one square vertically, or two squares vertically and one square horizontally.

Write a function to determine the minimum number of moves required for the knight to move from the starting position (0, 0) to the target position (x, y). Assume that it is always possible to reach the target position, and that x and y are both integers in the range [-200, 200]

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: The knight can move from (0, 0) to (1, 2) in one move.

Example 2:
Input: x = 4, y = 4
Output: 4
Explanation: The knight can move from (0, 0) to (4, 4) in four moves ( [0, 0] -> [2, 1] -> [4, 2] -> [6, 3] -> [4, 4] )
"""

from collections import deque
class Solution:
    def minimumKnightMoves(self, x: int, y: int) -> int:
        """
        Time Complexity: O(n^2) -> O(max(x, y)^2)
        Space Complexity: O(n^2) -> O(max(x, y)^2)
        """
        directions = [
            (2, 1), (1, 2), 
            (-2, -1), (-1, -2), 
            (2, -1), (1, -2),
            (-2, 1), (-1, 2)
        ]
        queue = deque([(0, 0, 0)])
        visited = set()
        while queue:
            a, b, moves = queue.popleft()
            if a == x and b == y:
                return moves
            visited.add((a, b))
            for dx, dy in directions:
                nx, ny = dx+a, dy+b
                if (nx, ny) not in visited:
                    queue.append((nx, ny, moves + 1))

class Solution2:
    def minimumKnightMoves(self, x: int, y: int) -> int:
        """
        Time Complexity: O(n^2) -> O(max(x, y)^2)
        Space Complexity: O(n^2) -> O(max(x, y)^2)
        """
        x, y = abs(x), abs(y)

        directions = [
            (2, 1), (1, 2),
            (-2, 1), (-1, 2),
            (2, -1), (1, -2),
            (-2, -1), (-1, -2)
        ]

        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}
        while queue:
            a, b, moves = queue.popleft()
            if a == x and b == y:
                return moves
            for dx, dy in directions:
                nx, ny = a + dx, b + dy
                # small negative allowed because knight may need to step back
                if nx >= -2 and ny >= -2 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
if __name__ == "__main__":
    print(Solution().minimumKnightMoves(2, 1))
    print(Solution().minimumKnightMoves(4, 4))
    