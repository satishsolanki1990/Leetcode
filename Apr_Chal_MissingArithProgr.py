'''
https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3716/

In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

A value from arr was removed that was not the first or last value in the array.

Given arr, return the removed value.



Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].

'''


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # step size
        r = round((arr[-1] - arr[0]) / len(arr))

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != r:
                return arr[i - 1] + r

        return arr[-1]