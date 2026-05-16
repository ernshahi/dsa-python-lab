"""

"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Brute Force Approach
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(gas)
        for i in range(n):
            curr_gas = 0
            for j in range(i, n + i):
                idx = j % n
                curr_gas += gas[idx]
                if curr_gas >= cost[idx]:
                    curr_gas -= cost[idx]
                else:
                    break
            else:
                return i
        return -1

    class Solution:
        def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            """
            Greedy Approach
            Time Complexity: O(n)
            Space Complexity: O(1)
            """
            if sum(gas) < sum(cost):
                return -1
            start, fuel = 0, 0
            for i in range(len(gas)):
                fuel += gas[i] - cost[i]
                if fuel < 0:
                    start = i + 1
                    fuel = 0
            return start

                
                
