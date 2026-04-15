"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


class Solution:
    def twoSum2(self, nums, target):
        """
        Brute force approach
        - iterate over all possible pairs of numbers
        - return the indices of the two numbers if they add up to the target

        time complexity: O(n^2)
        space complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hashmap approach
        - iterate over the array
        - calculate the remaining value
        - if the remaining value is in the hashmap, return the indices
        - if the remaining value is not in the hashmap, add the current value to the hashmap

        time complexity: O(n)
        space complexity: O(n)
        """
        hashmap = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if hashmap.get(remaining) is not None:
                return hashmap[remaining], index
            hashmap[num] = index


if __name__ == "__main__":
    tests = [
        {"input": ([2, 7, 11, 15], 9), "output": (0, 1)},
        {"input": ([3, 2, 4], 6), "output": (1, 2)},
        {"input": ([3, 3], 6), "output": (0, 1)},
    ]

    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.test_runner import TestCaseRunner

    TestCaseRunner().run(tests, Solution().twoSum)
