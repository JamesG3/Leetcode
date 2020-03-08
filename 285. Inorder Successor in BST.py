# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.pval = p.val
        self.node = None
        
        self.traverse(root)
        return self.node
        
    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        if not self.node and node.val > self.pval:
            self.node = node
        self.traverse(node.right)

'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Solution: In order traversal
Time: O(n)
'''
        
