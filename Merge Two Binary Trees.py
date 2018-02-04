# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None

        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1

        elif not t1 and t2:
            return t2
        
        elif t1 and not t2:
            return t1
        
        
        
#         if t1 is None and t2 is None:
#             return
        
#         if t1:
#             v1 = t1.val
#             Left1 = t1.left
#             Right1 = t1.right
#         else:
#             v1 = 0
#             Left1 = None
#             Right1 = None
        
#         if t2:
#             v2 = t2.val
#             Left2 = t2.left
#             Right2 = t2.right
#         else:
#             v2 = 0
#             Left2 = None
#             Right2 = None
            
#         node = TreeNode(v1+v2)
#         node.left = self.mergeTrees(Left1, Left2)
#         node.right = self.mergeTrees(Right1, Right2)
        
#         return node
            
        
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        # Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
        # You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
        # Otherwise, the NOT null node will be used as the node of new tree.
        
