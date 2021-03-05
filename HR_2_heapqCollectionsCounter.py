'''
https://www.hackerrank.com/challenges/most-commons/problem

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.

'''

import collections
import heapq

if __name__ == '__main__':
    s = input()
    s = collections.Counter(list(s))
    s = list((-v, k) for k, v in s.items())
    heapq.heapify(s)
    for i in range(3):
        temp = heapq.heappop(s)
        print(temp[1], -temp[0])



