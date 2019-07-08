# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root != None:
            l=self.maxDepth(root.left)
            r=self.maxDepth(root.right)
            return max(l+1,r+1)
        else:
            return 0
        """
        :type root: TreeNode
        :rtype: int
        """
        