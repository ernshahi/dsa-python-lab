from typing import List


class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force approach
        - sort the array
        - iterate over the array
        - for each element, iterate over the array again
        - for each pair, iterate over the array again
        - if the sum of the three elements is 0, add the triplet to the result
        - return the result

        Time complexity: O(n^3)
        Space complexity: O(n)
        """
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tripplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(tripplet)
        return [list(res) for res in result]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Two pointers approach
        - sort the array
        - iterate over the array
        - for each element, use two pointers to find the other two elements that sum to 0
        - if the sum of the three elements is 0, add the triplet to the result
        - return the result

        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        nums = sorted(nums)
        result = []
        for i, val in enumerate(nums):
            if i > 0 and nums[i - 1] == val:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = val + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


if __name__ == "__main__":
    tests = [
        {"input": ([-1, 0, 1, 2, -1, -4],), "output": [[-1, -1, 2], [-1, 0, 1]]},
        {"input": ([0, 0, 0],), "output": [[0, 0, 0]]},
    ]
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.test_runner import TestCaseRunner

    TestCaseRunner().run(tests, Solution().threeSum)
