def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int

    Leetcode Problem 704: Binary Search
    https://leetcode.com/problems/binary-search/
    Difficulty: Easy

    Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
    If target exists, then return its index, otherwise return -1.

    """
    left = 0
    right = len(nums)-1
    mid = (right + left) // 2
    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
            mid = (right + left) // 2
        elif nums[mid] > target:
            right = mid -1
            mid = (right + left) // 2
    return -1

#test cases
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
print(search(nums, target))

