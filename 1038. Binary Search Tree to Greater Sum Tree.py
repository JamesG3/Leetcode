# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.accu_sum = 0
        self.helper(root)
        return root
        
        
    def helper(self, node):
        if not node:
            return
        
        self.helper(node.right)
        node_val = node.val
        node.val += self.accu_sum
        self.accu_sum += node_val
        self.helper(node.left)
        
        
'''
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Solution: Right-first in order traverse (desc order BST traverse)
Time: O(n)
Space: O(1)
'''
