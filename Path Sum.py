# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        else:
            if sum-root.val==0 and root.left is None and root.right is None:
                return True
        return self.hasPathSum(root.right,sum-root.val) or self.hasPathSum(root.left,sum-root.val)
        
        #move to left node and right node recursively, if one way is True, then the result is true
        #read all the leaves
        
        
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
        """
        
