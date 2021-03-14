'''
Given an array of meeting time intervals intervals
where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

'''

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals):
        heapify(intervals)
        # traverse through each meeting and check if any conference room vacent
        rooms = {}
        ans = 0
        room_assigned = False
        while intervals:
            meeting = heappop(intervals)
            # print(meeting,ans)
            for room in rooms:
                room_assigned = False
                if rooms[room] <= meeting[0]:
                    rooms[room] = meeting[1]
                    room_assigned = True
                    break

            if not room_assigned:
                ans += 1
                rooms[ans] = meeting[1]

        return ans

s=Solution
intervals = [[0,30],[5,10],[15,20]]
print(s.minMeetingRooms(intervals))