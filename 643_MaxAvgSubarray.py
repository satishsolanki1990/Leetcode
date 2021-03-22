'''
Given an array consisting of n integers,
find the contiguous subarray of given length k that has the maximum average value.
And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

'''


class Solution:
    def findMaxAverage(self, nums, k) :
        p1 = 0
        p2 = p1 + k
        cur_sum = sum(nums[p1:p2])
        ans = -float('inf')
        n = len(nums)
        while p2 <= n:
            ans = max(ans, cur_sum / k)
            if p2 < n:
                cur_sum = cur_sum - nums[p1] + nums[p2]
            p2 += 1
            p1 += 1

        return ans


s=Solution()
nums=[1,12,-5,-6,50,3]
k=4

print(s.findMaxAverage(nums,k))