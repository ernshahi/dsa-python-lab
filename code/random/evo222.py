from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort(reverse=True)
        result = 0
        loop_range = len(nums)//2
        print(f"nums: {nums}")
        print(f"loop_range: {loop_range}")
        
        for i in range(loop_range):
            result += nums[i] * nums[i]
            print(f"i: {i}, result: {result}, num: { nums[i]}")
            
        print(f"*******")
            
        for i in range(-1, -loop_range-1, -1):
            result -= nums[i] * nums[i]
            print(f"i: {i}, result: {result}, num: { nums[i]}")

        if len(nums) % 2 == 1:
            result += nums[loop_range] * nums[loop_range]
            print(f"result: {result}, num: { nums[i]}")
        return result
    

if __name__ == "__main__":
    print(Solution().maxAlternatingSum([1,2,3])) # 12
    if not grid: return -1
        queue = deque([])
        rows, cols = len(grid), len(grid[0])
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time_to_rott = 0
        while queue and fresh > 0: 
            time_to_rott += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1

        return time_to_rott if fresh == 0 else -1
