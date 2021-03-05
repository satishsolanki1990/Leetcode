'''
Given k sorted arrays, can you sort all of them into one ascending order array.

Example:
arr = [

    [2, 4, 8, 10],
    [1, 3, 9],
    [11, 12, 14],
    [100, 102, 500]
]
Output = [1, 2, 3, 4, 8, 9, 10, 11, 12, 14, 100, 102, 500]
'''

import heapq

def merge_k(arr):
    # Initalize
    init_heap = [(sub_ar[0], ind, 0) for ind, sub_ar in enumerate(arr)]
    heapq.heapify(init_heap)

    out = []
    # iterate through the loop
    while (init_heap):

        cur_min = heapq.heappop(init_heap)
        out.append(cur_min[0])
        if cur_min[2] < len(arr[cur_min[1]]) - 1:
            # print(cur_min)
            sub_arr_ind = cur_min[1]
            sub_arr_pos = cur_min[2] + 1

            to_push = (arr[sub_arr_ind][sub_arr_pos], sub_arr_ind, sub_arr_pos)

            heapq.heappush(init_heap, to_push)

    # return
    return out


arr = [
    [2, 4, 8, 10],
    [1, 3, 9],
    [11, 12, 14],
    [100, 102, 500]
]

# What's the time complexity?
# O(nlog(k)) -> Perfect! Well done guys :D
#
print(merge_k(arr))

