from typing import List
from math import ceil

class Solution:
    def minHarvestRate3(self, apples: List[int], h: int) -> int:
        def _helper(rate):
            total_hrs = 0
            for apple in apples:
                total_hrs += ceil(apple/rate)
            return total_hrs
        rate = 1
        while _helper(rate) >  h:
            rate += 1
        return rate
            
    def minHarvestRate(self, apples: List[int], h: int) -> int:
        def _helper(rate):
            total_hrs = 0
            for apple in apples:
                total_hrs += ceil(apple/rate)
            return total_hrs
        left, right = 1, max(apples)
        while left < right:
            mid = (left + right) // 2
            if _helper(mid) > h:
                left = mid + 1
            else:
                right = mid
        return left
                
        
            
if __name__ == "__main__":
    apples = [25, 9, 23, 8, 3]
    h = 5
    print(Solution().minHarvestRate(apples, h))