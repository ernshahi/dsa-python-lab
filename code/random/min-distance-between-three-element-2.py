from typing import List

# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         min_dist = float('inf')
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] == nums[j] == nums[k]:
#                         min_dist = min(min_dist, abs(i-j) + abs(j-k) + abs(k-i))
#         return -1 if min_dist == float('inf') else min_dist

# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         """first try just for info: but it desn't work for all test cases"""
#         min_dist = float('inf')
#         for i in range(len(nums)-2):
#             j, k = i+1, i + 2
#             while j < k and j < len(nums) - 2 and k < len(nums) - 1:
#                 if nums[i] == nums[j] == nums[k]:
#                     min_dist = min(min_dist, abs(i-j) + abs(j-k) + abs(k-i))
#                     break
#                 elif nums[i] == nums[j]:
#                     k += 1
#                 elif nums[i] == nums[k]:
#                     j, k = k, k + 1
#                 else:
#                     j = k + 1
#                     k = k + 2
#         return -1 if min_dist == float('inf') else min_dist
    
#     def minimumDistance3(self, nums: List[int]) -> int:
#         min_dist = float('inf')
#         temp = nums
#         map = dict()
#         for i, val in enumerate(temp):
#             if val not in map:
#                 map[val] = []
#             map[val].append(i)
#         for vals in map.values():
#             if len(vals) > 2:
#                 for i in range(2, len(vals)):
#                     a, b, c = vals[i - 2], vals[i - 1], vals[i]
#                     min_dist = min(min_dist, abs(a -b) + abs(b-c) + abs(c-a))
#         return -1 if min_dist == float('inf') else min_dist
    
    
# if __name__ == "__main__":
#     print(Solution().minimumDistance3([2, 1, 2, 3, 2, 4, 2]))
#     print(Solution().minimumDistance3([5,5,5,2,5]))



class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        def backtrack(i, j, k, val):
            if i >= rows or j >= cols:
                return -1
            if grid[i][j] == 0:
                pass
            elif grid[i][j] == 1:
                val += 1
                k -= 1
            else: # == 2
                val += 2
                k -= 1
            if k < 0:
                return -1
            if i == rows -1 and j == cols-1:
                return val
            return max(backtrack(i+1, j, k, val), backtrack(i, j+1, k, val))
        return backtrack(0, 0, k, 0)
    
if __name__ == "__main__":
    grid = [[0, 1],[1, 2]]
    k = 1
    print(Solution().maxPathScore(grid=grid, k=k))