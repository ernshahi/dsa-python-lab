"""
DESCRIPTION
Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

Input:
intervals = [(1,5),(3,9),(6,8)]
Output:
false
Explanation: The meetings (1,5) and (3,9) overlap.

Input:
intervals = [(10,12),(6,9),(13,15)]
Output:
true
"""

class Solution:
    def canAttendMeetings1(self, intervals: list[list[int]]):
        """
        This is a brute force solution that sorts the intervals and checks for overlapping meetings.
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
    
    def canAttendMeetings(self, intervals: list[list[int]]):
        """
        This is a more efficient solution that only checks for overlapping meetings.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]

        for i in range(1, len(intervals)):
            current_s = intervals[i][0]
            if prev_s < current_s < prev_e:
                return False
            prev_s = current_s
            prev_e = intervals[i][1]
        return False
    

if __name__ == "__main__":
    intervals = [(1,5),(3,9),(6,8)]
    print(Solution().canAttendMeetings(intervals)) # False

    intervals = [(10,12),(6,9),(13,15)]
    print(Solution().canAttendMeetings(intervals)) # True