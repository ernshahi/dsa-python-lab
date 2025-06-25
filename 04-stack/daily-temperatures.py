"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

class Solution:
    def dailyTemperatures1(self, temps: list[int]):
        """
        Time: O(n^2)
        Space: O(n)
        Idea:
        - Use a stack to track the indices of the temperatures
        - For each temperature, check if the next temperature is greater
        """
        stack = [0] * len(temps)
        for i in range(len(temps)):
            for j in range(i+1, len(temps)):
                if temps[j] > temps[i]:
                    stack[i] = j-i
                    break
        return stack
    
    def dailyTemperatures(self, temps: list[int]):
        """
        Time: O(n)
        Space: O(n)
        Idea:
        - Use a stack to track the temperatures
        - For each temperature, check if the next temperature is greater using the monotonic stack
        - If it is not, pop the stack and update the result
        - stack is a stack of tuples (temp, index)
        """
        result = [0] * len(temps)
        stack = [] # (temp, index)

        for i, temp in enumerate(temps):
            while stack and stack[-1][0] < temp:
                stackT, stackInx = stack.pop()
                result[stackInx] = i - stackInx
            stack.append([temp, i])
        return result

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([65, 70, 68, 60, 55, 75, 80, 74])) # [1,4,3,2,1,1,0,0]
