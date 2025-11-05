"""
Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)

Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False
"""

class Solution:
    def is_pair_sum_brute_force(self, nums, k):
        """Brute force approach"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == k:
                    return True
        return False
    def is_pair_sum(self, nums, k):
        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                return True
            if curr_sum < k:
                left += 1
            else:
                right -= 1
        return False
    
if __name__ == "__main__":
    print(Solution().is_pair_sum(nums=[1,3,4,6,8,10,13], k=13))