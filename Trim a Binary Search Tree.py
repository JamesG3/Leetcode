# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        if root is None:
            return
        if root.val < L:                    # if smaller, look its right child
            return self.trimBST(root.right, L, R)
        elif root.val > R:                  # if larger, look its left child
            return self.trimBST(root.left, L, R)
        else:                               # if root.val is in the range, traverse its left and right children
            root.left = self.trimBST(root.left, L, R)   # trim node which is not in the range
            root.right = self.trimBST(root.right, L, R)
            return root

# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). 
# You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
        
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
