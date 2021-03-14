'''
973

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e, √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

'''

from heapq import *


class Solution:
    def kClosest(self, points, k) :
        # compute dist
        d = [(sqrt(x[0] ** 2 + x[1] ** 2), x) for x in points]
        heapify(d)  # O(log(N)) # This is O(n) -> heapifying is linear, #got it

        res = []
        for i in range(k):
            res.append(heappop(d))

        return res


# time complexity = O(klog(n)) ->
# bit high space complexity


'''
        # Will klogn > n log k or vice versa?  
        # i think so too! let's use mathss

        # k log n -> n is 10000 and k is 3. 12
        # 10000 log(3) = 477.12  yours is better definitely! AH butt
        # It's interesting!! Will have to do a deeper analysis 
        # yeahh. It is . 


        """
        Runtime: 672 ms, faster than 66.22% of Python3 online submissions for K Closest Points to Origin.
        Memory Usage: 20 MB, less than 44.17% of Python3 online submissions for K Closest Points to Origin.
        """

'''