# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return []
        result = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.left)]
        result += [str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]
        return result or [str(root.val)]
        
        
        #Given a binary tree, return all root-to-leaf paths.
