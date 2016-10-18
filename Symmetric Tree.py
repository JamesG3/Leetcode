# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:                                        # For situation []
            return True
        return self.recursive(root.left, root.right)
        
        
    def recursive(self, left, right):
        if left != None and right != None:
            if left.val == right.val:
                return self.recursive(left.left, right.right) and self.recursive(left.right, right.left)    # check all points from start to leaves
            else:
                return False
        else:
            if left == right:                                   # check if left and right are both null
                return True
            else:
                return False
        """
        :type root: TreeNode
        :rtype: bool
        
        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
        """
        
