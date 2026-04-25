"""
Given a sorted array nums, a target value target, and an integer k, find the k closest elements to target in the array, where "closest" is the absolute difference between each element and target. Return these elements in array, sorted in ascending order.

Example 1:

Inputs:
nums = [-1, 0, 1, 4, 6]
target = 1
k = 3
Output:
[-1, 0, 1]


Explanation: -1 is 2 away from 1, 0 is 1 away from 1, and 1 is 0 away from 1. All other elements are more than 2 away. Since we need to return the elements in ascending order, the answer is [-1, 0, 1]
Example 2:

Inputs:
nums = [5, 6, 7, 8, 9]
target = 10
k = 2

[8, 9]
"""
from typing import List
import heapq

class Solution:
    def kClosest(self, nums: List[int], k: int, target: int) -> List[int]:
        arr = [(-abs(target-num), num) for num in nums]
        heap = arr[:k]
        heapq.heapify(heap)
        for curr in arr[k:]:
            if curr[0] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, curr)
        return [num[1] for num in heap]
    
if __name__ == "__main__":
    print(Solution().kClosest([-1, 0, 1, 4, 6], 3, 1)) # -1, 0, 1
    print(Solution().kClosest([5, 6, 7, 8, 9], 2, 10)) # 8, 9