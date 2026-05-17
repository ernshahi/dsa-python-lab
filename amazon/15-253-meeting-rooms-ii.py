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
        starts = sorted([ interval.start for interval in intervals ]) # [0,5,15]
        ends = sorted([ interval.end for interval in intervals ]) # [10,20,30]
        rooms, max_rooms = 0, 0
        curr_start, curr_end = 0, 0
        while curr_start < len(intervals):
            if starts[curr_start] < ends[curr_end]: 
                # if start time of current meeting is before end time of current room, we need a new room
                rooms += 1
                curr_start += 1
                max_rooms = max(max_rooms, rooms)
            else:
                # if start time of current meeting is after end time of current room, we can use the current room
                rooms -= 1
                curr_end += 1
        return max_rooms