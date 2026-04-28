"""
4-binary-tree-zigzag-level-order-traversal.py
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        left_to_right = True
        while queue:
            length = len(queue)
            curr_nodes = []
            for _ in range(length):
                node = queue.popleft()
                curr_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left_to_right:
                result.append(curr_nodes)
            else:
                result.append(curr_nodes[::-1])
            left_to_right = not left_to_right
        return result

    def zigzagLevelOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        left_to_right = True
        while queue:
            length = len(queue)
            curr_nodes = deque()
            for _ in range(length):
                node = queue.popleft()
                if left_to_right:
                    curr_nodes.append(node.val)
                else:
                    curr_nodes.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(curr_nodes))
            left_to_right = not left_to_right
        return result
                

                
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))