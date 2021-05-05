'''
3. Longest Substring Without Repeating Characters

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
from collections import *
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        l_ptr=0 # left ptr
        used=defaultdict(int)
        for r_ptr,val in enumerate(s):
            if val in used and l_ptr <= used[val]:
                left = used[val]+1
            else:
                ans = max(ans,r_ptr-l_ptr+1)
            used[val]=r_ptr
        return ans


sol=Solution()
# s="abcabcbb"
s="dvdf"
print(sol.lengthOfLongestSubstring(s))
