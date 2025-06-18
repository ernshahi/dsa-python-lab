"""
2461. Maximum Sum of Distinct Subarrays With Length K
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left, max_sum, current_sum = 0, 0, 0
        count = {}
        for right in range(len(nums)):
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            if right - left + 1 > k:
                current_sum -= nums[left]
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
    print(sol.maximumSubarraySum([4, 4, 4], 3))