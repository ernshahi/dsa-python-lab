"""

"""
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map = {}
        for i, char in enumerate(s):
            last_index_map[char] = i
        result = []
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, last_index_map[char])
            if i == end:
                result.append(end-start+1)
                start = end + 1
        return result

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Brute Force Approach
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Less Preferred Approach
        """
        result = []
        start = 0
        while start < len(s):
            end = start
            i = start
            while i <= end:
                end = max(end, s.rfind(s[i]))
                i += 1
            result.append(end - start + 1)
            start = end + 1
        return result
    
    def partitionLabels(self, s: str) -> List[int]:
        """
        Greedy Approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        last_index_map = {}
        for i, char in enumerate(s):
            last_index_map[char] = i
        result = []
        start = end = 0
        for i, char in enumerate(s):
            end = max(end, last_index_map[char])
            if i == end:
                result.append(end-start+1)
                start = end + 1
        return result