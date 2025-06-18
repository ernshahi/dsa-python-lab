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
class Solution:
    def maxScore(self, cards: list[int], k: int):
        """
        This is a sliding window problem.
        We can use a sliding window to find the maximum sum of any contiguous subarray of size k.

        Time complexity: O(k)
        Space complexity: O(1)
        """
        max_sum = 0
        current_sum = sum(cards[:k])
        max_sum = current_sum
        for i in range(1, k+1):
            current_sum -= cards[k-i]
            current_sum += cards[-i]
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore([2,11,4,5,3,9,2], 3)) # 17
    print(sol.maxScore([1,2,3,4,5,6,1], 3)) # 12