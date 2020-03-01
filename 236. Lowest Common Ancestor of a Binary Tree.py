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
        self.ans = None
        
        self.helper(root)
        return self.ans
    
    def helper(self, node):
        if not node:
            return False
        
        left, right = self.helper(node.left), self.helper(node.right)
        if left == right == False and node in (self.q, self.p):
            return True
        
        elif (left or right) and node in (self.q, self.p):
            self.ans = node
            return True
        
        elif left and right:
            self.ans = node
            return True
        
        else:
            return (left or right)
        
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Solution: Recursive, backtracking
Time: O(n)
'''
