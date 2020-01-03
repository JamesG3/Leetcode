# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == root2:
            return True
        if (not root1) or (not root2):
            return False
        
        return [i for i in self.get_leaves(root1)] == [i for i in self.get_leaves(root2)]
        
        
    def get_leaves(self, node):
        if (not node.left) and (not node.right):
            yield node.val
            
        else:
            if node.left:
                yield from self.get_leaves(node.left)
            if node.right:
                yield from self.get_leaves(node.right)
                
'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

Solution: Tree traverse, find all the leaves, use recursion using yield generator
Time, Space: O(n)
'''
