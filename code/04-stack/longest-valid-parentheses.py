"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
                continue
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
        return max_length

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.longestValidParentheses("(()"))  # Output: 2
    print(solution.longestValidParentheses(")()())"))  # Output: 4
    print(solution.longestValidParentheses(""))  # Output: 0
    print(solution.longestValidParentheses("()(()")) # Output: 2
    print(solution.longestValidParentheses("()()")) # 4