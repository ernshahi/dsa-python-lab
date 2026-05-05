"""
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy Approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Much Preferred Approach
        """
        if not nums:
            return False
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
    
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy Approach
        Time Complexity: O(n)
        Space Complexity: O(1)

        Less Preferred Approach
        """
        if not nums:
            return False
        curr_max = nums[0]
        for i in range(1, len(nums)):
            if curr_max <= 0:
                return False
            curr_jumps = nums[i]
            curr_max = max(curr_max - 1, curr_jumps)
        return True
