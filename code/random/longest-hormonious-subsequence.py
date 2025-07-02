"""
594. Longest Harmonious Subsequence
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.
"""
from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # c = defaultdict(int)
        # for n in nums:
        #     c[(n, n+1)] += 1
        #     c[(n-1, n)] += 1
        # nums = set(nums)
        
        # result = 0
        # for m, n in c.items():
        #     if m[0] in nums and m[1] in nums:
        #         result = max(result, n)
        # return result

        c = Counter(nums)
        result = 0
        for m, n in c.items():
            if m + 1 in c:
                result = max(result, n + c.get(m+1))
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # Output: 5
    print(s.findLHS([1, 2, 3, 4]))              # Output: 2
    print(s.findLHS([1, 1, 1, 1]))              # Output: 0