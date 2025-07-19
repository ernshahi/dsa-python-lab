"""Visit all the nodes in matrix"""

def dfs(matrix):
    visited = set()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    def dfs_helper(r, c):
        if (r, c) in visited:
            return
        if r < 0 or r >= len(matrix[0]) or c < 0 or c >= len(matrix):
            return
        visited.add((r, c))
        print(matrix[r][c])

        for rd, cd in directions:
            dfs_helper(r+rd, c+cd)
    dfs_helper(0, 0)

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    dfs(matrix)