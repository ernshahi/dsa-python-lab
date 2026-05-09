"""
496. Next Greater Element I
"""
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Brute Force
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        res = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            found = False
            for num_2 in nums2:
                if found and nums2 > num:
                    res[i] = num_2
                    break
                if num_2 == num:
                    found = True
        return res
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Optimized using hash map and stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        next_greater = { num: -1 for num in nums2 }
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        result = []
        for num in nums1:
            result.append(next_greater[num])
        return result
                
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Optimized using hash map and stack with index
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nums_res = { num: -1 for num in nums2 }
        stack = [] # 0
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                nums_res[nums2[index]] = nums2[i]
            stack.append(i)
        res = []
        for num in nums1:
            res.append(nums_res[num]) 
        return res

    
    
if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])) # [-1, 3, -1]