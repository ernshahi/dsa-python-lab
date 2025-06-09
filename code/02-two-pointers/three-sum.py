class Solution:
    def threeSum(self, nums: list[int]):
        # Your code goes here
        result = {}
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                for third in range(first + 2, len(nums)):
                    if nums[first] + nums[second] + nums[third] == 0:
                        result[(nums[first], nums[second], nums[third])] = ""
        return [list(item) for item in result.keys()]


if __name__ == "__main__":
    tests = [
        {"input": [-1, 0, 1, 2, -1, -1], "output": [[-1, -1, 2], [-1, 0, 1]]},
        {"input": [0, 0, 0], "output": [[0, 0, 0]]},
    ]

    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.test_runner import TestCaseRunner

    TestCaseRunner().run(tests, Solution().threeSum)
