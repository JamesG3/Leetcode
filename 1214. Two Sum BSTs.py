# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
# class Solution:
    # @lru_cache(None)
    # def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
#         if not (root1 and root2):
#             return False
        
#         if root1.val + root2.val == target:
#             return True
        
#         elif root1.val + root2.val > target:
#             return self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1, root2.left, target)
#         elif root1.val + root2.val < target:
#             return self.twoSumBSTs(root1.right, root2, target) or self.twoSumBSTs(root1, root2.right, target)

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        l1 = self.traverse(root1, [])
        l2 = self.traverse(root2, [])
        
        p1, p2 = 0, len(l2) - 1
        len1 = len(l1)
        
        while p1 < len1 and p2 > 0:
            if l1[p1] + l2[p2] == target:
                return True
            
            elif l1[p1] + l2[p2] < target:
                p1 += 1
            else:
                p2 -= 1    
        return False
        
        
            
    def traverse(self, node, lst):
        if not node:
            return
        
        self.traverse(node.left, lst)
        lst.append(node.val)
        self.traverse(node.right, lst)
        return lst
    
    
'''
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree 
whose values sum up to a given integer target.

Solutions: 
    1. BST search with LRU cache (slower, would be TLE if without LRU cache)
    2. Convert BST into lists, two pointers solution, read from start of one tree and end of another (Faster)
'''
