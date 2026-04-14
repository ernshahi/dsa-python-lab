from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cursor = 0
        for idx, val in enumerate(nums):
            if val == 0:
                nums[idx], nums[cursor] = nums[cursor], nums[idx]
                cursor += 1
        left = cursor
        right = len(nums) - 1
        # [0,0,0,1,1,1,1,2,2]
        while left < right:
            while nums[left] == 1:
                left += 1
            while nums[right] == 2:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors(nums = [2,1,2,0,1,0,1,0,1]))
    

