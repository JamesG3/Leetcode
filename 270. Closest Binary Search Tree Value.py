# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        iterator = self.iterator(root)
        res = float('inf')
        cnter = 0
        
        while True:
            try:
                nxt = iterator.__next__()
                if abs(nxt - target) < abs(res - target):
                    res = nxt
                    continue
                
                # early termination
                cnter += 1
                if cnter > 2:
                    break
                
            except:
                break
        return res
        
        
        
    def iterator(self, node):
        if not node:
            return
        
        yield from self.iterator(node.left)
        yield node.val
        yield from self.iterator(node.right)
        
'''
Solution: BST, generator, recursive, early termination
Time: O(1) - O(n)
Space: O(h)
'''
