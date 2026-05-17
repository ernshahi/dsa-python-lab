"""
49. Group Anagrams
https://www.hellointerview.com/community/questions/group-anagrams/cm5eh7nrh04od838oi2p9pzk1?company=Amazon

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Hashmap and Sorting Approach
        Time Complexity: O(n * k log k)
        Space Complexity: O(n * k)
        """
        mapping = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            mapping[key].append(word)
        return list(mapping.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Hashmap and Counting Approach
        Time Complexity: O(n * k * 26) -> O(n * k)
        Space Complexity: O(n * k)
        """
        mapping = defaultdict(list)
        for word in strs:
            count = [0] * 26 # a ... z
            for char in word:
                count[ord(char) - ord('a')] += 1
            mapping[tuple(count)].append(word)
        return [ val for key, val in mapping.items()]
            