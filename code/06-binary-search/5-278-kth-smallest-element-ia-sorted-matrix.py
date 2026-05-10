"""
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        rows, cols = len(matrix), len(matrix[0])
        def _count_less_than_or_equal_to(num):
            count = 0
            r, c = rows - 1, 0
            while r >= 0 and c <= cols - 1:
                if matrix[r][c] <= num:
                    count += r + 1
                    c += 1
                else:
                    r -= 1
            return count >= k
        while left <= right:
            mid = (left + right) // 2
            if _count_less_than_or_equal_to(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time Complexity: O(n^2 log n^2) because of the sorting
        Space Complexity: O(n^2) because of the extra flattened list
        """
        flat_matrix = [ i for row in matrix for i in row ]
        flat_matrix.sort()
        return flat_matrix[k-1]
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        rows, cols = len(matrix), len(matrix[0])
        def helper(num):
            count = 0
            r, c = rows - 1, 0
            while r >= 0 and c <= cols - 1:
                if matrix[r][c] <= num:
                    count += r + 1
                    c += 1
                else:
                    r -= 1
            return count >= k

        for i in range(left, right+1):
            if helper(i):
                return i
        return -1
