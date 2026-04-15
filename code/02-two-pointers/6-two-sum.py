"""
DESCRIPTION
Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.

Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)

Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False
"""


class Solution:
    def isPairSum2(self, nums, target):
        """
        Brute force approach
        - iterate over all possible pairs of lines
        - check sum of pair equls to target
        - return True if equal else check next Pair

        time complexity: O(n^2)
        space complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return True
        return False

    def isPairSum(self, nums, target):
        """
        Two pointers approach
        - initialize two pointers, left and right, to the start and end of the array
        - calculate the sum of the elements at the two pointers
        - if the sum is equal to the target, return True
        - if the sum is greater than the target, move the right pointer inward
        - if the sum is less than the target, move the left pointer inward

        time complexity: O(n)
        space complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return True
            if curr_sum > target:
                right -= 1
            else:
                left += 1
        return False


if __name__ == "__main__":
    tests = [
        {"input": ([1, 3, 4, 6, 8, 10, 13], 13), "output": True},
        {"input": ([1, 3, 4, 6, 8, 10, 13], 6), "output": False},
    ]

    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.test_runner import TestCaseRunner

    TestCaseRunner().run(tests, Solution().isPairSum)
