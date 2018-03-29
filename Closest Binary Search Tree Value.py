# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        res = root.val
        
        while root:
            if abs(res - target) > abs(root.val-target):
                res = root.val
            if target>root.val:
                root = root.right
            else:
                root = root.left
        return res
                
        
        
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        
        # Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
        # Note:
        # Given target value is a floating point.
        # You are guaranteed to have only one unique value in the BST that is closest to the target.
