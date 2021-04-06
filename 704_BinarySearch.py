'''
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

'''


class Solution:
    def search(self, nums, target):
        n = len(nums)

        l = 0
        r = n - 1
        # iterative method
        mid = 0

        def recursiveSearch(l, r):
            if l > r:
                return -1
            nonlocal mid, target
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return recursiveSearch(l, mid - 1)
            else:
                return recursiveSearch(mid + 1, r)

        return recursiveSearch(l, r)

        # iterative method
        # while(l<=r):
        #     mid = l+(r-l)//2
        #     if target == nums[mid]:
        #         return mid
        #     elif target < nums[mid]:
        #         r=mid-1
        #     else:
        #         l=mid+1
        #
        # return -1


s=Solution()

nums = [-1,0,3,5,9,12]
target = 9

print(s.search(nums,target))