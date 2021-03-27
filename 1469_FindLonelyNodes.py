'''
In a binary tree, a lonely node is a node that is the only child of its parent node.
The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of
all lonely nodes in the tree. Return the list in any order.


Example 1:

Input: root = [1,2,3,null,4]
Output: [4]
Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def getLonelyNodes(self, root):
        if root.left == None and root.right == None:
            return

        if root.left == None or root.right == None:
            if root.left == None: self.ans.append(root.right.val)
            if root.right == None: self.ans.append(root.left.val)

        if root.left != None: self.getLonelyNodes(root.left)
        if root.right != None: self.getLonelyNodes(root.right)

        return self.ans