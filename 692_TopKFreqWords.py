'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower
alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding",'i','i'], k = 2
{i:2,love:2,leetcode:1,coding:1} O(n)

heapify O(n)

klog(n)

Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
'''
from collections import *
from heapq import *


class Solution:
    def topKFrequent(self, words, k):
        '''
        # logic: create a hashmap, and store the frequency of each

        '''
        # hash the words
        hashmap = defaultdict(int)
        for i in words:
            hashmap[i] += 1

        heap = [(-v, k) for k, v in hashmap.items()]
        heapify(heap)

        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])

        return ans


#https: // leetcode.com / problems / top - k - frequent - words /

s = Solution()

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

print(s.topKFrequent(words, k))