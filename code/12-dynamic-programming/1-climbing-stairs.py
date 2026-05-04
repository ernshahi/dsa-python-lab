"""
70. Climbing Stairs
Example 1:

Input: n = 2

Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Optimized Bottom Up Approach
        Time: O(n)
        Space: O(1)
        """
        if n <= 2:
            return n
        prev, curr = 1, 2
        for i in range(2, n):
            prev, curr = curr, prev + curr
        return curr
    
    def climbStairs2(self, n: int) -> int:
        """
        Bottom Up Approach with Tabulation
        Time: O(n)
        Space: O(n)
        """
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    
    def climbStairs3(self, n: int) -> int:
        """
        Top Down Approach Brute Force
        Time: O(2^n)
        Space: O(n)
        """
        if n <= 2:
            return n
        return self.climbStairs3(n-1) + self.climbStairs3(n-2)
    
    
    memo = {}
    def climbStairsHelper(self, n: int) -> int:
        """
        Top Down Approach with Memoization
        Time: O(n)
        Space: O(n)
        """
        if n in self.memo:
            return self.memo[n]
        if n <= 2:
            return n
        self.memo[n] = self.climbStairsHelper(n-1) + self.climbStairsHelper(n-2)
        return self.memo[n]
    
    