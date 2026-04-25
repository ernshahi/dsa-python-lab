"""
1448. Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    result = 0
    def helper(self, node, max_val):
        if node is None:
            return 
        if node.val >= max_val:
            self.result += 1
            max_val = node.val
        self.helper(node.left, max_val)
        self.helper(node.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def helper(node, max_val):
            nonlocal result
            if node is None:
                return 
            if node.val >= max_val:
                self.result += 1
                max_val = node.val
            helper(node.left, max_val)
            helper(node.right, max_val)
        helper(root, float('-inf'))
        return self.result
            

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(5)
    print(Solution().goodNodes(root))
