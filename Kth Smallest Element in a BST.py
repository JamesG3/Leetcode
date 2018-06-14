# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.traverse(root)
        return self.res
        
        
    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.traverse(node.right)
        
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        
        # Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
        # You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

