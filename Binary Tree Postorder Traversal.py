# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        res=[]
        self.helper(root,res)
        return res
        
        
    def helper(self, root, res):
        if root==None:
            return
        self.helper(root.left,res)
        self.helper(root.right,res)
        res.append(root.val)
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
