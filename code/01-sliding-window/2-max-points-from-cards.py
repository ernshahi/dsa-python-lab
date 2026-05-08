"""
1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

Given an array of integers representing the value of cards, write a function to calculate the maximum score you can achieve by selecting exactly k cards from either the beginning or the end of the array.

For example, if k = 3, then you have the option to select:

the first three cards,
the last three cards,
the first card and the last two cards
the first two cards and the last card
Example 1: 
Input:
cards = [2,11,4,5,3,9,2]
k = 3

17
"""
from typing import List

class Solution:
    def maxScore(self, cards: list[int], k: int):
        """
        Try every split:
        take i cards from the right
        and k-i cards from the left.

        Time: O(k)
        Space: O(1)
        """
        current_sum = sum(cards[:k])
        max_sum = current_sum
        for i in range(1, k+1):
            current_sum -= cards[k-i]
            current_sum += cards[-i]
            max_sum = max(max_sum, current_sum)
        return max_sum

class Solution2:
    def maxScore(self, cards: List[int], k: int) -> int:
        """
        Sliding window:
        we keep a window of size len(cards) - k
        and we slide it across the cards array.
        at each step, we update the maximum sum.

        Time: O(n)
        Space: O(1)
        """
        max_sum = float('-inf')
        curr_sum = start = 0
        total = sum(cards)
        if len(cards) == k: # edge case when we take all cards
            return total
        for end in range(len(cards)):
            curr_sum += cards[end]
            if end - start + 1 == len(cards) - k:
                max_sum = max(max_sum, total-curr_sum)
                curr_sum -= cards[start]
                start += 1
        return max_sum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore([2,11,4,5,3,9,2], 3)) # 17
    print(sol.maxScore([1,2,3,4,5,6,1], 3)) # 12