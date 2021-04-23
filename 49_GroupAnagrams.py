'''
Given an array of strings strs, group the anagrams together. You can return the answer
 in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]

'''

'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'eat' = 'aet'
chr(): 
ord()
list of [0]*27
a = 1
b = 2
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for strings in strs:
            l = [0] * 26
            for char in strings:
                idx = ord(char) - 97
                l[idx] += 1
            key = tuple(l)
            d[key].append(strings)

        return [val for key, val in d.items()]

        # d=defaultdict(list) # to store words
        # for strings in strs:
        #     key=''.join(sorted(strings))
        #     d[key].append(strings)

        # return [val for key,val in d.items()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

s = Solution()
print(s.groupAnagrams(strs))