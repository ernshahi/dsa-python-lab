"""
Given a sorted array of integers nums and a target value target, write a function to determine if target is in the array. If target is present in the array, return its index. Otherwise, return -1.

Example 1:
nums = [-1,0,3,5,9,12], target = 9
Output: 4 (nums[4] = 9)


Example 2:
nums = [-1,0,3,5,9,12], target = 2 # 0, 5, 2 # 0, 1
Output: -1 (2 is not in the array)
"""

class Solution:
    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
        
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    nums = [-1,0,3,5,9,12]
    target = 2
    print(Solution().binary_search(nums, target))