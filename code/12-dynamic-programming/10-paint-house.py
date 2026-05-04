"""
Paint House

You are a renowned painter who is given a task to paint n houses in a row. You can paint each house with one of three colors: Red, Blue, or Green. The cost of painting each house with each color is different and given in a 2D array costs:
costs[i][0] = cost of painting house i Red
costs[i][1] = cost of painting house i Blue
costs[i][2] = cost of painting house i Green
No two neighboring houses can have the same color. Return the minimum cost to paint all houses.

Constraints:
1 ≤ n ≤ 100
costs[i].length == 3
1 ≤ costs[i][j] ≤ 1000

Example 1
Input:
costs = [[8, 4, 15], [10, 7, 3], [6, 9, 12]]
Output:
13

Explanation:
House 0: Blue (cost = 4)
House 1: Green (cost = 3)
House 2: Red (cost = 6)
Total = 4 + 3 + 6 = 13

Example 2
Input:
costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 5, 9]]
Output:
30
Explanation: Red(5) → Green(13) → Red(7) → Blue(5) = 30
"""
from typing import List

class Solution:
    def min_cost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        prev, curr = None, costs[0]
        for i in range(1, len(costs)):
            temp = curr.copy()
            curr = [
                costs[i][0] + min(temp[1], temp[2]),
                costs[i][1] + min(temp[0], temp[2]),
                costs[i][2] + min(temp[0], temp[1])
            ]
            prev = temp
        return min(curr)

class Solution:
    def min_cost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        memo = {}
        def _helper(h, prev_color):
            result = float('inf')
            if h == n:
                return 0
            if (h, prev_color) in memo:
                return memo[(h, prev_color)]
            for color in [0, 1, 2]:
                if prev_color is None or color != prev_color:
                    cost = costs[h][color] + _helper(h+1, color)
                    result = min(result, cost)
            memo[(h, prev_color)] = result
            return result
        
        return _helper(0, None)
