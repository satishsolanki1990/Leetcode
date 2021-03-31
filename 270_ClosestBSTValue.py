'''
Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.

Example:
Input: root = [4,2,5,1,3],
target = 3.714286
Output: 4

logic:
1. first we check if node is not root

[4,2,5,1,3]
ans
min= inf
root     diff                  global min     ans
4     abs(3.714286 - 4)           =0.29        4
2     abs((3.714286 - 2)=1.7      =0.29        4
1     abs((3.714286 - 1)=2.7      =0.29        4
3     abs((3.714286 - 3)=0.7      =0.29        4
.
.
.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # if tree is empty:
        if root == None:
            return -1
        ans = 0
        global_min = float('inf')

        def recursive(root):
            nonlocal ans, global_min
            # base case
            if root == None:
                return

            # check if distance of val is less than min
            if abs(target - root.val) <= global_min:
                ans = root.val
                global_min = abs(target - root.val)

            if target < root.val:
                recursive(root.left)
            else:
                recursive(root.right)

        recursive(root)

        return ans
