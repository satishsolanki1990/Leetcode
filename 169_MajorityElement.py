"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n / 2

"""
class Solution:
    def majorityElement(self, nums):
        '''
        logic: keep track of numbers in hashmap(dict) with track of maxterm and maxcount
        if count of any term is more than maxcount then save maxterm
        :  no need to go through entire list if we find majority term earlier.
        '''
        if len(nums) <= 2:
            return nums[0]

        count = {}
        maxterm = None
        maxcount = 0
        n=len(nums)//2
        for i in nums:
            if maxcount > n :
                break
            if i in count:
                count[i] += 1
                if count[i] > maxcount:
                    maxterm = i
                    maxcount = count[i]
            else:
                count[i] = 1

        return maxterm


sol=Solution()
nums=[3,2,3]
print(sol.majorityElement(nums))