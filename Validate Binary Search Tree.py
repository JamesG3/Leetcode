# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        sort=[]
        self.inorderTraversal(root, sort)
        
        for i in xrange(len(sort)-1):
            if sort[i] >= sort[i+1]:
                return False
        return True
    
    def inorderTraversal(self, root, sort):
        if root==None:
            return
        
        self.inorderTraversal(root.left, sort)
        sort.append(root.val)
        self.inorderTraversal(root.right, sort)
        
        
        """
        :type root: TreeNode
        :rtype: bool
        """

        #Given a binary tree, determine if it is a valid binary search tree (BST).
