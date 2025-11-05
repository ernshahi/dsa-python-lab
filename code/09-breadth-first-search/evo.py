from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    
    def __init__(self):
        pass

    def bfs(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            current = queue.popleft()
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
            

class Solution2:
    def level_dfs(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            items = []
            for _ in range(level_length):
                current = queue.popleft()
                items.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(items)
        return result
            
            
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
    # inputs = [1, 3, 4, None, 2, 7, None, 8]
    # print(Solution().level_sum(input)) # Output: [1, 7, 9, 8]
    nums = [-3,-1,-2,1,3,2]
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    nums.sort(reverse=True)
    print(nums)