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
            total = sum(math.ceil(apple/mid) for apple in apples)
            if total <= h:
                result = mid
                right = mid - 1 # # try smaller k as user prefer slower as much as possible
            else: 
                left = mid + 1 # # need to eat faster as consumed hrs is more than given limit
        return result
    


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minHarvestRate(piles, h))  # Output: 4
    
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(Solution().minHarvestRate(piles, h))  # Output: 30