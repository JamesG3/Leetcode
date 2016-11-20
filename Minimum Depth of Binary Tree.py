# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        
        result=[]
        self.helper(root, 1, result)
        return min(result)
        
    def helper(self, root, depth, result):
        if root.left:
            self.helper(root.left, depth+1, result)
        if root.right:
            self.helper(root.right, depth+1, result)
        elif root.left is None and root.right is None:          #leaf=> depth of this branch
            result.append(depth)
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #Given a binary tree, find its minimum depth.
        #The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
