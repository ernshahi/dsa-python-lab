"""
435. Non-Overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

from typing import List

class Solution:

    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)

        This is a greedy algorithm that sorts the intervals by their end time and then iterates through the intervals to find the minimum number of intervals to remove.
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return len(intervals) - count

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(1)

        This is a greedy algorithm that sorts the intervals by their start time and then iterates through the intervals to find the minimum number of intervals to remove.
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        result = 0
        pointer = intervals[0][1]
        n = len(intervals)

        for j in range(1, n):
            if pointer > intervals[j][0]:
                result += 1
                pointer = min(pointer, intervals[j][1])
            else:
                pointer = max(pointer, intervals[j][1])
        return result
    
    
if __name__ == "__main__":
    # print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 
    # print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
    # print(Solution().eraseOverlapIntervals([[1,2],[2,3]])) # 0
    print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])) # 2
