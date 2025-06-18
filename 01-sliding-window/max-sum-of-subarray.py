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

class Solution:
    def max_subarray_sum(self, nums, k):
        left, result, curr_sum = 0, 0, 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            if right - left < k:
                result = max(result, curr_sum)
            else:
                curr_sum -= nums[left]
                result = max(result, curr_sum)
                left += 1
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.max_subarray_sum([2, 1, 5, 1, 3, 2], 3))


