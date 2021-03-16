'''
You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from heapq import *

class Solution:
    def mergeKLists(self, lists):

        heap = [(listnode.val, position) for position, listnode in enumerate(lists) if listnode]
        output = ListNode(0)
        temp = output
        heapify(heap)

        while (heap):
            val, position = heappop(heap)
            temp.next = ListNode(val)
            temp = temp.next
            if lists[position].next:
                lists[position] = lists[position].next
                push_val = lists[position].val
                heappush(heap, (push_val, position))

        return output.next