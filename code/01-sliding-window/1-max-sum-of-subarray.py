"""
https://www.hellointerview.com/learn/code/sliding-window/fixed-length

DESCRIPTION
Given an array of integers nums and an integer k, find the maximum sum of any contiguous
subarray of size k

.
Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.
"""
from typing import List

class Solution:
    def max_subarray_sum(self, nums, k):
        start, max_sum, window_sum = 0, float('-inf'), 0

        for end in range(len(nums)):
            window_sum += nums[end]
            if end - start == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[start]
                start += 1
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
    print(sol.max_subarray_sum([2, 1, 5, 1, 3, 2], 222))


