# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Solution: Tree traverse (reversed inorder)
        Time: O(n)
        Space: O(1)
        """
        self.sum = 0
        self.traverse(root)
        return root
        
    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.right)
        tmp = node.val
        node.val += self.sum
        self.sum += tmp
        self.traverse(node.left)
        
        
# Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
