"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""
from typing import List

# Brute force approach
# Time complexity: O(n^2)
# Space complexity: O(1)
def largestRectangleArea(heights):
    max_area = 0
    n = len(heights)

    for i in range(n): 
        left = i - 1
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1

        right = i + 1
        while right < n and heights[right] >= heights[i]:
            right += 1

        max_area = max(max_area, (right - left - 1) * heights[i])
    
    return max_area

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for idx, val in enumerate(heights):
            start = idx
            while stack and val <= stack[-1][-1]:
                i, h = stack.pop()
                max_area = max(max_area, (idx-i) * h)
                start = i
            stack.append((start, val))
        for idx, val in stack:
            max_area = max(max_area, (len(heights) - idx) * val)
        return max_area

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3])) # 10
    print(sol.largestRectangleArea([2,4])) # 4