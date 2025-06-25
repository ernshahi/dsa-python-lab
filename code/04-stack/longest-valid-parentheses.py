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
        """
        Time: O(n)
        Space: O(1)
        Idea:
        - Use two pointers to track the longest valid parentheses substring
        - left and right are the number of left and right parentheses respectively
        - if left == right, then the substring is valid, update mx
        - if right > left, then the substring is invalid, reset left and right
        - do the same for the reversed string, as first loop doesn't work for cases like "((()"
        """
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
        """
        Time: O(n)
        Space: O(n)
        Idea:
        - Use a stack to track the indices of the left parentheses
        - if the current character is a right parenthesis, pop the stack
        - if the stack is empty, push the current index
        - if the stack is not empty, update the maximum length
        - stack is [-1] to handle the case when the first character is a right parenthesis
        """
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