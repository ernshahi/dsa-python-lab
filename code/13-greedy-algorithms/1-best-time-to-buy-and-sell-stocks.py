"""

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        profit = 0
        buy = sell = prices[0]
        for price in prices:
            if price < buy:
                buy = sell = price
            elif price > sell:
                sell = price
            profit = max(profit, sell - buy)
        return profit