"""
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 
"""

from typing import List
from collections import Counter, defaultdict

class Solution:
    def totalFruit1(self, fruits: List[int]) -> int:
        fruitCounter = Counter(fruits)
        import pdb; pdb.set_trace()
        return sum(sorted(fruitCounter.values())[-2:])
    
    def totalFruit2(self, fruits: List[int]) -> int:
        maxCount = 0
        for i in range(len(fruits)):
            for j in range(i, len(fruits)):
                if len(set(fruits[i:j+1])) < 3:
                    maxCount = max(maxCount, j - i +1)
                else:
                    break
        return maxCount
    
    def totalFruit3(self, fruits: List[int]) -> int:
        maxCount = 0
        for i in range(len(fruits)):
            state = {}
            for j in range(i, len(fruits)):
                state[fruits[j]] = state.get(fruits[j], 0) + 1
                if len(state) < 3:
                    maxCount = max(maxCount, j - i +1)
                else:
                    break
        return maxCount
    
    def totalFruit(self, fruits: List[int]) -> int:
        state  = defaultdict(int)
        left, result, total = 0, 0, 0
        for right in range(len(fruits)):
            state[fruits[right]] += 1
            total += 1
            while len(state) > 2:
                state[fruits[left]] -= 1
                total -= 1
                if state[fruits[left]] == 0:
                    del state[fruits[left]]
                left += 1
            result = max(result, total)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([1,2,1])) # 3
    print(sol.totalFruit([0,1,2,2])) # 3
    print(sol.totalFruit([1,2,3,2,2])) # 4
    print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5