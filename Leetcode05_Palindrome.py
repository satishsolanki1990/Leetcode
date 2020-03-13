"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # method 2 (better than 33.48%)
        if x<0:
            return False
        elif x<10:
            return True
        else:
            l=list(str(x))
            lr=l[::-1]
            if (x-int("".join(lr))) != 0:
                return False
            else:
                return True
'''
# mehthod 1 (better than 19%)
        import math
        if x<0:
            return False
        elif x<10:
            return True
        else:
            l=list(str(x))
            for i in range(int(math.floor(len(l)/2))):
                if l[i] != l[len(l)-1-i]:
                    return False
            return True
'''

