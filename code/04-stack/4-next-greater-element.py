"""
DESCRIPTION
Given an array of integers, find the next greater element for each element in the array. The next greater element of an element x is the first element to the right of x that is greater than x. If there is no such element, then the next greater element is -1.
Example
Input: [2, 1, 3, 2, 4, 3]
Output: [3, 3, 4, 4, -1, -1]
"""

def nextGreaterElement(nums):
  n = len(nums)
  result = [-1] * n
  stack = []
  for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
      index = stack.pop()
      result[index] = nums[i]
    stack.append(i)
  return result

"""
Next Smaller Element
"""

def nextSmallerElement(nums):
  n = len(nums)
  result = [-1] * n
  stack = []
  for i in range(n):
    while stack and nums[i] < nums[stack[-1]]:
      index = stack.pop()
      result[index] = nums[i]
    stack.append(i)
  return result