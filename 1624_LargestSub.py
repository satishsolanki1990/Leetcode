"""
Given a string s, return the length of the longest substring between two equal characters,
excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        max_sub = -1
        # convert into dict
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = i
            else:
                max_sub = max(max_sub, i - d[ch] - 1)

        return max_sub

sol = Solution()
s = "cabbac"
print(sol.maxLengthBetweenEqualCharacters(s))