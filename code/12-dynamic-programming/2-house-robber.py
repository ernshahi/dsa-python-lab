"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        return max(dp[len(nums)], dp[len(nums)-1])

        # Optimal space solution
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = curr
            curr = max(prev + nums[i], temp)
            prev = temp
        return max(prev, curr)

        # recursive solution
        def _helper(n):
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            skip = _helper(n-1)
            take = _helper(n-2) + nums[n-1]
            return max(skip, take)
        return _helper(len(nums))

        # memoization solution
        memo = {}
        def _helper(n):
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n in memo:
                return memo[n]
            skip = _helper(n-1)
            take = _helper(n-2) + nums[n-1]
            memo[n] = max(skip, take)
            return memo[n]
        return _helper(len(nums))

