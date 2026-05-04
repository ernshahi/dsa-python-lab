"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
"""

from typing import List
import math


class Solution:
    def minHarvestRate(self, apples: List[int], h: int):
        left, right = 1, max(apples)
        result = right

        while left <= right:
            mid = (left + right) // 2
            total = 0
            for apple in apples:
                total += math.ceil(apple/mid)
            if total <= h:
                result = mid
                right = mid - 1 # # try smaller k as user prefer slower as much as possible
            else: 
                left = mid + 1 # # need to eat faster as consumed hrs is more than given limit
        return result
    

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def _can_eat(speed):
            hours_taken = 0
            for pile in piles:
                hours_taken += ceil(pile/speed)
                if hours_taken > h:
                    return False
            return True
        # naive approach:
        # max(piles) * n
        # rate = 1
        # while _helper(rate) > h:
        #     rate += 1
        # return rate
        
        # binary search approach:
        left, right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            if _can_eat(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minHarvestRate(piles, h))  # Output: 4
    
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(Solution().minHarvestRate(piles, h))  # Output: 30