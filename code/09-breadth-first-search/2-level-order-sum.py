"""
DESCRIPTION
Given the root of a binary tree, return the sum of the nodes at each level. The output should be a list containing the sum of the nodes at each level.

Example 1:
Input:
[1, 3, 4, null, 2, 7, null, 8]

Output:
[1, 7, 9, 8]
"""
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level_order_sum(self, root: TreeNode):
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            level_sum = 0
            level_length = len(queue)
            for _ in range(level_length):
                current_node = queue.popleft()
                level_sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(level_sum)
        return result
    
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(3, TreeNode(4), TreeNode(2, TreeNode(7), TreeNode(8))))
    print(Solution().level_order_sum(root)) # Output: [1, 7, 9, 8]