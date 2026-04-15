# Two Pointers 
ref: https://www.hellointerview.com/learn/code/two-pointers/overview

Two pointer is a algorithm which uses two pointers that starts at the opposite ends of an array and move towards each other until they meet.

- Two pointers is an algorithm pattern that uses two pointers to traverse an array or list. 
- The two pointers are usually initialized to the start and end of the array or list.
- The two pointers are then moved towards each other until they meet.
- The two pointers are usually used to find a pair of elements in an array or list that satisfy a certain condition.
- List must be sorted for two pointers to work.

## Problems
- Two sum
- Container with most water
- Three sum

```python

def two_sum2(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    return False

if __name__ == "__main__":
    nums = [1,3,4,6,8,10,13]
    target = 13
    print(two_sum(nums, target))
```