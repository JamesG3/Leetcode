# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [root]
        while True:
            tmp_stack = []
            res = 0
            for item in stack:
                res += item.val
                if item.left:
                    tmp_stack.append(item.left)
                if item.right:
                    tmp_stack.append(item.right)
            if not tmp_stack:
                break
                
            stack = tmp_stack
                
        return res
                
                
            
'''
Given a binary tree, return the sum of values of its deepest leaves.

Solution: BFS, tree level traversal
Time, Space: O(n)
'''
            
        
