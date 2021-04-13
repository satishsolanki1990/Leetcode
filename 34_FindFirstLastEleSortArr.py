'''
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

 Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

'''

class Solution:
    def searchRange(self, nums, target):
        # find target
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if l > r: return [-1, -1]

        # at this point, we have l,r, and mid
        mid_r = mid  # use in first occurance seach
        mid_l = mid  # use in last occurance search

        # search for first occurance
        while (l <= mid_r):
            if nums[l] == target:
                break
            mid = l + (mid_r - l) // 2
            if nums[mid] == target:
                mid_r = mid - 1
            else:
                l = mid + 1

        while (r >= mid_l):
            if nums[r] == target:
                break
            mid = mid_l + (r - mid_l) // 2
            if nums[mid] == target:
                mid_l = mid + 1
            else:
                r = mid - 1

        return [l, r]