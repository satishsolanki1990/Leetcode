"""
1351. Count Negative Numbers in a Sorted Matrix

Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

"""

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # with sort
        # Runtime: 104 ms, faster than 73.81% 
        count=0
        for i in grid:
            i.sort()
            for j in i:
                if j>=0:
                    break
                else:
                    count+=1
        
        return count
                
        # without sort 
        # 96 ms, faster than 97.12% 
        
        count=0
        
        for i in grid:
            for j in i:
                if j<0:
                    count+=1
        
        return count
                    
        
