"""
1732 :
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

"""
class Solution:
    def largestAltitude(self, gain) :
        max_alt = 0
        alt = 0
        for i in gain:
            alt += i
            max_alt = max(max_alt, alt)

        return max_alt


sol=Solution()
gains=[-5,1,5,0,-7]
print(sol.largestAltitude(gains))