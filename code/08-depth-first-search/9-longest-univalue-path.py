"""
687. Longest Univalue Path
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
Example 1:
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).

Example 2:
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_ = 0
        def dfs(node):
            nonlocal max_
            if node is None: return 0
            if not node.left and not node.right:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_arrow, right_arrow = 0, 0
            if node.left and node.left.val == node.val:
                left_arrow = left + 1
            if node.right and node.right.val == node.val:
                right_arrow = right + 1
            max_ = max(max_, (left_arrow + right_arrow))
            return max(left_arrow, right_arrow)
        dfs(root)
        return max_
            
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root))