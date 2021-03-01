'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Recursion
        if x>0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        c=recursive(x)
        c=sign*c
        if c<=(2**31 - 1) and c>= -(2**31) :
            return int(c)
        else:
            return 0
'''        
        # Brut Force
        import math
        c=0
        l=len(str(abs(x)))
        if x>0:
            sign=1
        else:
            sign=-1
        x=abs(x)
        for i in range(l):
            r=x%10
            c+=(r*10**(l-i-1))
            x=math.floor(x/10)
        
        c=sign*c
        if c<=(2**31 - 1) and c>= -(2**31) :
            return int(c)
        else:
            return 0
'''
def recursive(x):
    import math
    if x<10:
        return x
    else:
        l=len(str(x))
        return (x%10)*(10**(l-1))+recursive(int(math.floor(x/10)))    
    
