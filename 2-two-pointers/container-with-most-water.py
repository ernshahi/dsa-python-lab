# https://leetcode.com/problems/container-with-most-water/description/
"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
import os, sys
from typing import List

class Solution:
    def maxArea2(self, height: List[int]) -> int:
        """
        Brute force approach
        - iterate over all possible pairs of lines
        - calculate the area of the container
        - update the result if the current area is greater
        
        time complexity: O(n^2)
        space complexity: O(1)
        """
        result = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j-i) * min(height[j], height[i])
                if area > result:
                    result = area
        return result
    
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers approach
        - initialize two pointers, left and right, to the start and end of the array
        - calculate the area of the container
        - update the result if the current area is greater
        - move the pointer that points to the shorter line inward

        time complexity: O(n)
        space complexity: O(1)
        """
        left, right = 0, len(height) - 1        
        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            if result < area: result = area
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return result


if __name__ == "__main__":
    tests = [
        { "input": [1,8,6,2,5,4,8,3,7], "output": 49},
        { "input": [1,1], "output": 1}
    ]

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils.test_runner import TestCaseRunner
    
    TestCaseRunner().run(tests, Solution().maxArea2)

