"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        charmap = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for char in s:
            if char in charmap.values():
                stacks.append(char)
            elif char in charmap:
                if not stacks or stacks[-1] != charmap[char]:
                    return False
                stacks.pop()
            else:
                return False
        return False if stacks else True

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()")) # True
    print(sol.isValid("()[]{}")) # True
    print(sol.isValid("(]")) # False
    print(sol.isValid("([]))")) # False