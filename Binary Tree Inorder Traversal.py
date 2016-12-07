# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        global res
        res=[]
        self.Traversal(root)
        return res
        
        
        
    def Traversal(self, root):
        global res
        if root is None:
            return
        self.Traversal(root.left)
        res.append(root.val)
        self.Traversal(root.right)
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
