'''
Given an array of integers nums,
sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1,
'1' has a frequency of 2, and '2' has a frequency of 3.

Input:
nums = [2,3,1,3,2]
[1,3,3]

Output: [1,3,3,2,2]
Explanation: '2' and '3'
both have a frequency of 2, so they are sorted in decreasing order.

# store num and fre d = {num:freq}

num=key and feq is value

nums = [2,3,1,3,2]

dic= {2:2,3:2,1:1}


minheap={(freq,-val)} (1,-1) (2,-3),(2,-2)

 pop out = (1,1) ans= [1]

 pop out = (2,3)

'''
from heapq import *
from collections import defaultdict,Counter

class Solution(object):
    def frequencySort(self, nums):
        freq=Counter(nums)

        nums.sort(key = lambda k: (freq[k],-k) )

        return nums




class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dictionary
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        # heapify
        temp = [(freq, -val) for val, freq in d.items()]
        heap = []
        for i in temp:
            heappush(heap, i)
        ans = []
        while heap:
            f, v = heappop(heap)
            temp = [-v] * f
            ans += temp

        return ans


s = Solution()
nums = [2, 3, 1, 3, 2]

print(s.frequencySort(nums))

print(s.frequencySort([1, 1, 2, 2, 2, 3]))
# head back 2 main room

