# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root)
        
    def helper(self, node):
        if not node:
                return float('inf')
    
        if (not node.left) and (not node.right):
            return 1
        
        return min(self.helper(node.left), self.helper(node.right)) + 1

'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
'''
