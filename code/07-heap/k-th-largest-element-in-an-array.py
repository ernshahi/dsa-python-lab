"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    print(solution.findKthLargest(nums, k))  # Output: 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(solution.findKthLargest(nums, k))  # Output: 4