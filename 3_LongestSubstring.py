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
        left=0
        used=defaultdict(int)
        for right,val in enumerate(s):
            if val in used and left <= used[val]:
                left = used[val]+1
            else:
                ans = max(ans,right-left+1)
            used[val]=right
        return ans


sol=Solution()
# s="abcabcbb"
s="dvdf"
print(sol.lengthOfLongestSubstring(s))
