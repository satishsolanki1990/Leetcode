"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        logic: for nums[i], if target-nums[i] in nums-> return indexes

        Since we need frequent search, we can use hash map
        '''

        hashmap = defaultdict(list)

        for i, v in enumerate(nums):
            hashmap[v].append(i)

        for k in hashmap:
            temp = target - k
            if temp in hashmap:
                if k != temp:
                    return [hashmap[k][0], hashmap[temp][0]]  # since there is unique element
                else:
                    if len(hashmap[k]) == 2:
                        return hashmap[k]