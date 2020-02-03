# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        return self.helper(root)
        
    def helper(self, node):
        if not node:
            return False
        
        l = self.helper(node.left)
        r = self.helper(node.right)
        
        if l and r:
            return node
        
        if isinstance(l, TreeNode):
            return l
        if isinstance(r, TreeNode):
            return r
        
        return (node in (self.p, self.q)) or (l or r)
            
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Solution: Tree DFS
'''
