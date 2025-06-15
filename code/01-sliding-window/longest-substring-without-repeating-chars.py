"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        maxLength = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                if len(s[left:right+1]) != len(set(s[left: right + 1])):
                    break
                maxLength = max(maxLength, right - left + 1)
        return maxLength
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, result = 0, 0
        state = []
        for r in range(len(s)):
            while s[r] in state:
                state.remove(s[l])
                l += 1
            state.append(s[r])
            result = max(result, r - l + 1)
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
    print(sol.lengthOfLongestSubstring("bbbbb")) # 1
    print(sol.lengthOfLongestSubstring("pwwkew")) # 3
    