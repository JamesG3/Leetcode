# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

# recursive solution
    def longestUnivaluePath(self, root):
        global mxlen
        mxlen = 0
        self.helper(root)
        return mxlen
        
        
    def helper(self, root):
        global mxlen
        
        if not root:
            return 0
        
        c1 = self.helper(root.left)
        c2 = self.helper(root.right)
        r, l = 0, 0
        if root.left and root.left.val == root.val:
            l = c1 + 1
        if root.right and root.right.val == root.val:
            r = c2 + 1
        mxlen = max(mxlen, l+r)
        return max(l, r)
            
        
        """
        :type root: TreeNode
        :rtype: int
        """

# Given a binary tree, find the length of the longest path where each node in the path has the same value. 
# This path may or may not pass through the root.

# Note: The length of path between two nodes is represented by the number of edges between them.
