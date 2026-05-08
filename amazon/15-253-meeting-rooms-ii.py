"""
Leetcode 253. Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Explanation:
room1: (0,40)
room2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([ interval.start for interval in intervals ])
        ends = sorted([ interval.end for interval in intervals ])
        count, max_count = 0, 0
        curr_start, curr_end = 0, 0
        while curr_start < len(starts):
            if ends[curr_end] > starts[curr_start]:
                count += 1
                curr_start += 1
                max_count = max(max_count, count)
            else:
                count -= 1
                curr_end += 1
        return max_count