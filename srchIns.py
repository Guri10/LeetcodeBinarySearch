
def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int

    Leetcode Problem 35: Search Insert Position
    https://leetcode.com/problems/search-insert-position/
    Difficulty: Easy

    Given a sorted array and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    You may assume no duplicates in the array.
    """

    left = 0
    right = len(nums)-1
    mid = (right + left) // 2

    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
            mid = (right + left) // 2
        elif nums[mid] > target:
            right = mid-1
            mid = (right + left) // 2
    return mid+1

#test cases
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))
