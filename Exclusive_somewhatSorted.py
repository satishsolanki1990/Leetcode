'''
You’re given a partially sorted array and k.
For example, [3, 1, 2, 7, 5, 6], where k = 2.
Each element is within +- k indices away from it’s correct position.

Can you sort the array, on average, in better than nlogn time complexity?

Example 1:
idx = 0 1 2 3 4 5
arr = [3, 1, 2, 7, 5, 6]
-2 -1 0 1 2

'''
from heapq import *


def sort(arr, k):
    res = []
    heap = arr[0:k]
    heapify(heap)
    i = k
    n = len(arr)
    while (i < n):
        res.append(heappop(heap))
        heappush(heap, arr[i])
        i += 1

    while heap:
        res.append(heappop(heap))

    return res


arr = [3, 1, 2, 7, 5, 6]
k = 2

print(sort(arr, k))
