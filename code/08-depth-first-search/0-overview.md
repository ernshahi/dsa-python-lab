# Depth First Search

## Tree Traversal Orders
| Traversal | Order               | Node timing |
| --------- | ------------------- | ----------- |
| Preorder  | Root → Left → Right | First       |
| Inorder   | Left → Root → Right | Middle      |
| Postorder | Left → Right → Root | Last        |

## [Fundamentals](https://www.hellointerview.com/learn/code/depth-first-search/fundamentals)

# Balanced Binary Tree
A binary tree is balanced if the height of the left and right subtrees of every node differ by at most 1.

# Complete Binary Tree
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. Complete binary trees are an important concept in heap data structures.

# Binary Search Tree
A binary search tree is a binary tree in which for each node, all nodes in the left subtree are less than the node, and all nodes in the right subtree are greater than the node.

# Skewed Binary Tree
A skewed binary tree is a binary tree in which all nodes are either on the left or right side of the tree.

# DFS:
DFS is a graph traversal algorithm that visits all the nodes of a graph depth-first. It starts at the root node and visits all the nodes in the tree by going as deep as possible before backtracking.

# BFS:
BFS is a graph traversal algorithm that visits all the nodes of a graph breadth-first. It starts at the root node and visits all the nodes in the tree by going as wide as possible before backtracking.

# Recursion and the Call Stack
DFS achieves backtracking through recursion.
A recursion function calls itself. The base case stops us from going past leaf nodes(base case).

# Example: Count Islands
```python
def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(r, c):
        if (r, c) in visited:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 1:
            return
        visited.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
```
