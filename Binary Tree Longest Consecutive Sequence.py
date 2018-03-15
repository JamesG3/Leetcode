# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0
    
    def longestConsecutive(self, root):
        self.helper(root)
        return self.ans
        
    def helper(self, node):
        if not node:
            return 0
        
        llen = rlen = 1
        l = self.helper(node.left)
        r = self.helper(node.right)
        
        
        if node.left and node.left.val-1 == node.val:
            llen = l + 1
        if node.right and node.right.val-1 == node.val:
            rlen = r + 1
        
        self.ans = max(self.ans, max(llen, rlen))
        return max(llen, rlen)
        
        
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        
# Given a binary tree, find the length of the longest consecutive sequence path.
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
# The longest consecutive path need to be from parent to child (cannot be the reverse).
        
