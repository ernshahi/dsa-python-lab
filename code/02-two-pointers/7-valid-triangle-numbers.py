"""
# 611. Valid Triangle Number

Given an integer array nums, 
return the number of triplets chosen from the array 
that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
"""
from typing import List

class Solution:
    def triangleNumber1(self, nums: List[int]) -> int:
        """
        Brute force approach
        - iterate over all possible triplets of lines
        - check if the triplet can form a triangle
        - return the number of valid triplets

        time complexity: O(n^3)
        space complexity: O(1)
        """
        result = 0
        nums.sort()
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                for k in range(j+1, size):
                    if nums[i] + nums[j] > nums[k]:
                        result += 1
        return result
    
    def triangleNumber2(self, nums: List[int]) -> int:
        """
        Two pointers approach
        - sort the array
        - iterate over the array
        - use two pointers to find the valid triplets
        - return the number of valid triplets

        time complexity: O(n^2)
        space complexity: O(1)
        """
        result = 0
        nums.sort()
        for k in range(2, len(nums)):
            l, r = 0, k-1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    result += (r-l)
                    r -= 1
                else:
                    i += 1
        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.triangleNumber1([2,2,3,4])) # 3
    print(sol.triangleNumber2([4,2,3,4])) # 4