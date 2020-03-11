'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        counter=1
        m=len(set(list(s)))
        if len(s)==m:
            return m
        else:
            for i in range(len(s)):
                if (is_in(l,s[i])==False):
                    l.append(s[i])
                    if i==(len(s)-1):
                        counter=max(counter,len(l)) 
                elif (l[-1]==s[i]):
                    counter=max(counter,len(l))
                    if counter == m:
                        return m
                    l=[]
                    l.append(s[i])
                else:
                    counter=max(counter,len(l))
                    if counter == m:
                        return m
                    temp=l.index(s[i])
                    l=l[temp+1:]
                    l.append(s[i])
        return counter

def is_in(l,a):
    try:
        temp=l.index(a)
        return True
    except ValueError:
        return False
