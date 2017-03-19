# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        if root is None:
            return 0
        global res
        res = []
        self.traverse(root)
        
        return max(res)
        
    def traverse(self, root):
        if root == None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        root.val = 1 + max(left, right)
        res.append(left+right)
        return root.val
        
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        #Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
