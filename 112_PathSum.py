'''
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such
that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

'''


class Solution:
    def hasPathSum(self, root, targetSum) :
        if root == None:
            return False

        def helper(run_sum, root):
            # base case
            if root.left == None and root.right == None:
                run_sum += root.val
                if run_sum == targetSum:
                    return True
                return False

            run_sum += root.val
            a = False
            b = False
            if root.left != None: a = helper(run_sum, root.left)
            if root.right != None: b = helper(run_sum, root.right)
            return a or b

        return helper(0, root)



