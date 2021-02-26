# 1413. Minimum Value to Get Positive Step by Step Sum
class Solution:
    def minStartValue(self, nums):
        '''
        logic: at any point running_sum + start_value > 0
        : start_value = 1 or abs(min of running_sum)+1)
        : keep track of minimum of running sum
        : if it is greater than one than return 1
        : else return abs(min of running sum)+1
        '''
        min_runsum = nums[0]
        runsum = 0
        for i in nums:
            runsum += i
            if runsum < min_runsum:
                min_runsum = runsum

        if min_runsum >= 1:
            return 1
        else:
            return abs(min_runsum) + 1


sol=Solution()
nums=[-3,2,-3,4,2]
# must return 5
print(sol.minStartValue(nums))