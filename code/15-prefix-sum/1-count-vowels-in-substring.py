"""
Count Vowels in Substrings

Write a function to efficiently count vowels within specified substrings of a given string.

The substrings will be given to you a list queries of [left, right] pairs, which correspond to the substring word[left:right + 1] in Python.

The function should return a list of integers, where each integer represents the vowel count for the corresponding query. You can assume the input string will only contain lowercase letters.

Your function should be optimized to run efficiently for a large number of queries.

Input:

word = "prefixsum"
queries = [[0, 2], [1, 4], [3, 5]]
Output: [1, 2, 1]

Explanation:

word[0:3] -> "pre" contains 1 vowels
word[1:5]-> "refi" contains 2 vowels
word[3:6]-> "fix" contains 1 vowels
"""
from typing import List

class Solution:
    def vowelStrings(self, word: str, queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i","o", "u"]
        prefix_sum = [0] * (len(word) + 1)
        curr_sum = 0
        for i in range(1, len(word) + 1):
            if word[i-1] in vowels:
                curr_sum += 1
            prefix_sum[i] = curr_sum
        result = []
        for x, y in queries:
            result.append(prefix_sum[y + 1] - prefix_sum[x])
        return result
