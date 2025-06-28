"""
2099. Find Subsequence of Length K With the Largest Sum
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
"""

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n log n)
        Space: O(n)
        Idea:
        - Sort the nums by value in descending order
        - Take the first k elements
        - Sort the result by index
        - Return the result
        """
        indexed_num = [(index, val) for index, val in enumerate(nums)]
        sorted_num = sorted(indexed_num, key=lambda x: x[1], reverse=True)

        result = sorted_num[:k]
        result.sort(key=lambda x: x[0])
        return [val for index, val in result]

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubsequence([2,1,3,3], 2)) # [3,3]
    print(sol.maxSubsequence([-1,-2,3,4], 3)) # [-1,3,4]
    print(sol.maxSubsequence([3,4,3,3], 2)) # [3,4]
