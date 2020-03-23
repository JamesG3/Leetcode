# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        self.L, self.R = L, R
        return self.helper(root)

        
    def helper(self, node):
        if not node:
            return None
        
        if node.val > self.R:
            return self.helper(node.left)
        
        if node.val < self.L:
            return self.helper(node.right)
        
        node.left = self.helper(node.left)
        node.right = self.helper(node.right)
        return node


'''
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Solution: Tree traversal, tree manipulation
Time: O(n)
'''
