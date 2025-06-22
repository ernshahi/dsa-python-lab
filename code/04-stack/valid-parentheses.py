"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

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
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in map.values(): 
                stack.append(char)
            elif char in map: 
                if not stack or  stack.pop() != map[char]:
                    return False
            else:
                return False
        return False if stack else True
            

if __name__ == "__main__":
    print(Solution().isValid("()")) # True
    print(Solution().isValid(r"()[]{}")) # True
    print(Solution().isValid("(]")) # False
    print(Solution().isValid("([])")) # True
