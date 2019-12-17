# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.helper(t)
        
    def helper(self, node):
        if not node:
            return ''
        
        if (not node.left) & (not node.right):
            return '{}'.format(node.val)
        
        if not node.right:
            return '{}({})'.format(node.val, self.helper(node.left))
        
        return '{}({})({})'.format(node.val, self.helper(node.left), self.helper(node.right))
    
    
'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Solution: Recursive tree traverse
Time & Space: O(n)
'''
