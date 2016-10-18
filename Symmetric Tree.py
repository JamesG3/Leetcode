# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.recursive(root.left, root.right)
        
        
    def recursive(self, left, right):
        if left != None and right != None:
            if left.val == right.val:
                return self.recursive(left.left, right.right) and self.recursive(left.right, right.left)
            else:
                return False
        else:
            if left == right:
                return True
            else:
                return False
        """
        :type root: TreeNode
        :rtype: bool
        """
        
