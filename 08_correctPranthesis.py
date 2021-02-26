"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # method 1:  faster than 97.26% ,memory use less than 42.02%
        stack=[]

        for i in s:
            if len(stack)==0:
                if i==')' or i=='}' or i==']':
                    return False
                else:
                    stack.append(i)
            else:
                if i==')':
                    if stack[-1]=='(':
                        stack.pop(-1)
                    else:
                        return False
                elif i=='}':
                    if stack[-1]=='{':
                        stack.pop(-1)
                    else:
                        return False
                elif i==']':
                    if stack[-1]=='[':
                        stack.pop(-1)
                    else:
                        return False
                else:
                    stack.append(i)

        if len(stack)==0:
            return True
        else:
            return False
