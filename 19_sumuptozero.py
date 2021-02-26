"""
1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

"""

class Solution:
    def sumZero(self, n) :
        '''
        logic: if n=odd then [-n//2...n//2]
        if n=even [-n/2....n/2] except 0
        '''

        if n % 2 != 0:
            return [x for x in range(-(n - 1) // 2, n // 2 + 1, 1)]
        else:
            return [x for x in range(-n // 2, n // 2 + 1, 1) if x != 0]


sol=Solution()
n=4

print(sol.sumZero(n))
