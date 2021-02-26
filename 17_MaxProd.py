"""
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different
indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

"""


class Solution:
    def maxProduct(self, nums):
        '''
        Logic: basically it is prod of highest and second highest

        '''
        highest = -float('inf')
        second = -float('inf')

        for i in nums:
            if i > second and i <= highest:
                second = i
            elif i > highest:
                second = highest
                highest = i

        return (highest - 1) * (second - 1)


sol=Solution()
nums= [3,4,5,2]
print(sol.maxProduct(nums))