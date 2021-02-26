"""
219. Contains Duplicate II

Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""
class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        '''
        Logic: using dictionary
        : for index, value in enum(nums):
        :   if dict has no value, store[value]=index
        :   else: if stored index - current index < k => return True
        : return false
        '''

        hashmap = {}

        for index, value in enumerate(nums):
            if not value in hashmap:
                hashmap[value] = index
            else:
                if index - hashmap[value] <= k:
                    return True
                else:
                    hashmap[value] = index

        return False


sol=Solution()
nums = [1,2,3,1]
k = 3
print(sol.containsNearbyDuplicate(nums,k))