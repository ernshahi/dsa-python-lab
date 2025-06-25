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
    def longestValidParentheses1(self, s: str) -> int:
        left = right = mx = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                mx = max(mx, left+right)
            elif right > left:
                left = right = 0
            
        left, right = 0, 0
        # for i in range(len(s) - 1, -1, -1):
        for c in reversed(s):
            if c == ")":
                right += 1
            else:
                left += 1
            if left == right:
                mx = max(mx, left + right)
            elif left > right:
                left = right = 0
        return mx
    
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
                continue
            stack.pop()
            if stack:
                mx = max(mx, i - stack[-1])
            else:
                stack.append(i)
        return mx


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.longestValidParentheses(")()())")) # output: 4
    print(solution.longestValidParentheses("(()"))  # Output: 2
    print(solution.longestValidParentheses(")()())"))  # Output: 4
    print(solution.longestValidParentheses(""))  # Output: 0
    print(solution.longestValidParentheses("()(()")) # Output: 2
    print(solution.longestValidParentheses("()()")) # 4