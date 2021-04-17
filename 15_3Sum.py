'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)
        for curr in range(n - 2):
            if curr > 0 and nums[curr - 1] == nums[curr]:
                continue
            l = curr + 1
            h = n - 1
            while (l < h):  # 1
                s = nums[curr] + nums[l] + nums[h]
                # case 1: s=0
                if s == 0:
                    ans.append([nums[curr], nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while (l < h and nums[l - 1] == nums[l]): l += 1
                    while (l < h and nums[h + 1] == nums[h]): h -= 1
                else:
                    if s > 0:  # case 2:
                        h -= 1
                        while (l < h and nums[h + 1] == nums[h]): h -= 1
                    else:  # case 3: s<0
                        l += 1
                        while (l < h and nums[l - 1] == nums[l]):  # 2
                            l += 1

        print(ans)
        return ans

