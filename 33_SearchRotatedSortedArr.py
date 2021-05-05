'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

# method -1
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                # left side is sorted
                if target >= nums[left] and target < nums[mid]:
                    # target is in sorted part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right side is sorted
                if target > nums[mid] and target <= nums[right]:
                    # target is in sorted part
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# method-2 : find pivot and then apply binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        left = 0
        right = len(nums) - 1
        pivot = 0
        while (left <= right):
            pivot = left + (right - left) // 2
            if pivot + 1 < len(nums) and nums[pivot] > nums[pivot + 1]:
                # we found the pivot
                pivot = pivot + 1
                break
            if nums[pivot] < nums[left]:
                # right part is sorted => pivot is in left
                right = pivot - 1
            else:
                left = pivot + 1

        if target >= nums[0] and target <= nums[pivot - 1]:
            # target is in left sorted region
            left = 0
            right = pivot
            while (left <= right):
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    # target is in right side
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            # target is in right sorted region
            left = pivot
            right = len(nums) - 1
            while (left <= right):
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    # target is in right side
                    left = mid + 1
                else:
                    right = mid - 1

        return -1