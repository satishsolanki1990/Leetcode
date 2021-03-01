"""
8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "   -42"
Output: -42

Input: "words and 987"
Output: 0

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # method 1:  faster than 14.94%,  memory use less than 10.00% 
        sign=1
        l=str.split()
        if len(l)==0:
            return 0
        else:
            try:
                x=int(l[0])
                if x<=(2**31 - 1) and x>(-2**31):
                    return x
                elif x<0:
                    return -2**31
                else:
                    return 2**31 - 1
            except:
                l=list(l[0])
                if l[0]=='-':
                    sign=-1
                    l.pop(0)
                elif l[0]=='+':
                    sign=1
                    l.pop(0)
                    
                num=[]
                for i in l:
                    try:
                        temp=int(i)
                        num.append(i)
                    except:
                        break
                if len(num)==0:
                    return 0
                else:
                    x=int(''.join([i for i in num]))

                if x <= ((2**31) - 1) and x >= ((-2)**31):
                    return sign*x
                elif (sign*x)<0:
                    return -2**31
                else:
                    return 2**31 - 1
            
                    
                
            
