"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        open == close == n -> add to res
        open == close and open < n: add open

        open > close and open < n --> both can be added
                                [""]
                                ["("]
                ["(("]                      ["()"]
        ["((("]             ["(()"]         ["()("]
        ["((()"]    ["(()("]    ["(())"]    ["()(("]    ["()()"]
        ["((())"]   ["(()()"]   ["(())("]   ["()(()"]   ["()()("]  
        ["((()))"]  ["(()())"]  ["(())()"]  ["()(())"]  ["()()()"]  
        """
        result = []
        def backtrack(open, close, curr):
            if open == close == n:
                result.append("".join(curr))
            if open < n:
                curr.append("(")
                backtrack(open+1, close, curr)
                curr.pop()

            if close < open:
                curr.append(")")
                backtrack(open, close+1, curr)
                curr.pop()
        backtrack(0, 0, [])
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(open, close):
            if open == close == n:
                result.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()
            return
        backtrack(0, 0)
        return result
