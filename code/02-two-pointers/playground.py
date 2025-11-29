
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