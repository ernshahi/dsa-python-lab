from typing import List

class Solution:
    def trap1(self, height: List[int]) -> int:
        """
        Brute force approach
        - iterate over the array
        - for each element, find the maximum height of the left and right pointers
        - calculate the amount of water trapped
        - return the total amount of water trapped
        """
        totalWater = 0
        for i in range(1, len(height)-1):
            left, right = i-1, i+1
            leftHeight, rightHeight = 0, 0
            while left > -1:
                if height[left] > leftHeight:
                    leftHeight = height[left]
                left -= 1
            while right < len(height):
                if height[right] > rightHeight:
                    rightHeight = height[right]
                right += 1
            possible_height = min(leftHeight, rightHeight)
            if possible_height > height[i]:
                totalWater += min(leftHeight, rightHeight) - height[i]
        return totalWater
    
    
    def trap(self, height: List[int]) -> int:
        """
        Two pointers approach
        - left pointer starts at the beginning of the array
        - right pointer starts at the end of the array
        - leftMax is the maximum height of the left pointer
        - rightMax is the maximum height of the right pointer
        - result is the total amount of water trapped
        - while left pointer is less than right pointer, calculate the amount of water trapped
        """
        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        result = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
    print(sol.trap1([3, 4, 1, 2, 2, 5, 1, 0, 2])) # 10
