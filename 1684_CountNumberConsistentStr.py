'''
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only
contain characters 'a' and 'b'.
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # convert into set
        a = set(allowed)
        count = 0
        for word in words:
            if set(word).union(a) == a:
                count += 1

        return count