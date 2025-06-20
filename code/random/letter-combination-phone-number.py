"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Time Complexity: O(4^n)
        Space Complexity: O(4^n)
        """
        if not digits:
            return []
        num_char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        for index, digit in enumerate(digits):
            if index == 0:
                result = list(num_char_map.get(digit))
                continue
            temp_result = []
            for char1 in result:
                for char2 in num_char_map.get(digit):
                    temp_result.append(f"{char1}{char2}")
            result = temp_result
        return result
                    

if __name__ == "__main__":
    print(Solution().letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(Solution().letterCombinations(""))