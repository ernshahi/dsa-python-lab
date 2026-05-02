"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List

class Solution2:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

if __name__ == "__main__":
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
    print(Solution().merge([[1,4],[4,5]])) # [[1,5]]