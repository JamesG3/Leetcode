# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxlen = 0
        
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Recursive solution, return the local longest path on each parent node, store global maxlen
        """
        if not root:
            return 0
        
        self.helper(root)
        return self.maxlen - 2
        
        
    def helper(self, node):
        if not node:
            return 0
        
        l_len, r_len = self.helper(node.left)+1, self.helper(node.right)+1
        self.maxlen = max(self.maxlen, l_len + r_len)
        return max(l_len, r_len)
        
