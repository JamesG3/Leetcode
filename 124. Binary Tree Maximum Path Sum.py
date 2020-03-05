# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = -float('inf')
        self.helper(root)
        
        return self.maxsum
        
    def helper(self, node):
        if not node:
            return 0
        # trick here: 
        # if the subtree sum is negative, then we cut it off, 
        # start a new path from the current node
        leftsum = max(self.helper(node.left), 0)
        rightsum = max(self.helper(node.right), 0)
        
        self.maxsum = max(self.maxsum, leftsum + rightsum + node.val)
        return max(leftsum, rightsum) + node.val
    

'''
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Solution: O(n)
Space: O(n)
'''
        
