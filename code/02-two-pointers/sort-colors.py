"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
 

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""
from typing import List

class Solution:
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = [], [], []
        for num in nums:
            if num == 0: red.append(num)
            if num == 1: white.append(num)
            if num == 2: blue.append(num)
        print(red + white + blue)
        return red + white + blue
    
    def sortColors3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0: red += 1
            if num == 1: white += 1
            if num == 2: blue += 1
        return [0]*red+[1]*white + [2]*blue
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1
        return nums

        
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))
    print(sol.sortColors([2,0,1]))