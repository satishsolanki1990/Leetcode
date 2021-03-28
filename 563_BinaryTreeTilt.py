'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all
left subtree node values and all right subtree node values.
If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
The rule is similar if there the node does not have a right child.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTilt(self, root) :
        self.global_tilt = 0
        # base case (hitting leaf node)
        if root == None:
            return 0

        total = self.helper(root, 0)
        # final return
        return self.global_tilt

    def helper(self, root, total):
        if root.left == None and root.right == None:
            return 0 + root.val  # total sum

        l_sum = 0
        r_sum = 0
        if root.left != None: l_sum = self.helper(root.left, total)
        if root.right != None: r_sum = self.helper(root.right, total)

        self.global_tilt += abs(l_sum - r_sum)
        total = root.val + l_sum + r_sum

        return total

