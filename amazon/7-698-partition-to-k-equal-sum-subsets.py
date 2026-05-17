"""
698. Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        used = [False] * len(nums)

        def backtrack(start, k, curr_sum):
            if k == 0:
                return True

            if curr_sum == target:
                return backtrack(0, k - 1, 0)

            prev = -1

            for j in range(start, len(nums)):
                if used[j]:
                    continue

                if nums[j] == prev:
                    continue

                if curr_sum + nums[j] > target:
                    continue

                used[j] = True

                if backtrack(j + 1, k, curr_sum + nums[j]):
                    return True

                used[j] = False

                prev = nums[j]

                # Important pruning:
                # If this number was tried as first item in empty bucket and failed,
                # no need to try other numbers as first item.
                if curr_sum == 0:
                    return False

                # If this number completed the bucket but still failed later,
                # no need to try other options for this bucket.
                if curr_sum + nums[j] == target:
                    return False

            return False

        return backtrack(0, k, 0)