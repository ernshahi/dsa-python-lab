"""
1482. Minimum Number of Days to Make m Bouquets
"""
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        left, right = min(bloomDay), max(bloomDay)

        def can_make(day):
            curr_flowers, curr_bouquets = 0, 0
            for bd in bloomDay:
                if bd <= day:
                    curr_flowers += 1
                    if curr_flowers == k:
                        curr_bouquets += 1
                        curr_flowers = 0
                else:
                    curr_flowers = 0
            return curr_bouquets >= m

        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left