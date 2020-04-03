# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pre = None
        self.a, self.b = None, None
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.a.val, self.b.val = self.b.val, self.a.val
        
    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        if self.pre and node.val < self.pre.val:
            # keep updating self.a ?? why, how to find the gapped elements to swap??
            self.a = node
            
            if self.b == None:
                self.b = self.pre
            else:
                return
        
        self.pre = node            
        self.traverse(node.right)
        
'''
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Solution: BST feature, in order traversal
Time: O(n)

'''
