# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return root

        self.Traversal(root)        #treversal tree and invert every node
        return root
        
    def Traversal(self, root):
        self.Invert(root)       #invert two subtree using Invert function
        if root.left!=None and root.right==None:        #traverse the only child of this node(if only one child)
            self.Traversal(root.left)
        elif root.left==None and root.right!=None:
            self.Traversal(root.right)
        elif root.left!=None and root.right!=None:      #two children-traverse both two children
            self.Traversal(root.left)
            self.Traversal(root.right)
        else:                   #if current node is leaf
            return
        
    def Invert(self, root):
        tem=root.right
        root.right=root.left
        root.left=tem

        
        
       #Invert a binary tree.
