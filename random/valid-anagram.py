"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        s_counter, t_counter = {}, {}
        if len(s) != len(t): return False

        for i in range(len(s)):
            s_counter[s[i]] = s_counter.get(s[i], 0) + 1
            t_counter[t[i]] = t_counter.get(t[i], 0) + 1

        for key in s_counter:
            if s_counter[key] != t_counter.get(key, 0):
                return False
        return True
        
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))  # Output: True

    s = "cat"
    t = "rat"
    print(solution.isAnagram(s, t))  # Output: False