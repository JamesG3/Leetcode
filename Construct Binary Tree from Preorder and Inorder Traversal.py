# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
    
        if len(preorder)==0 or len(inorder)==0:
            return None
        
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        #print inorderIndex
        #print preorder[1:inorderIndex+1]
        #print inorder[:inorderIndex]
        root.left = self.buildTree(preorder[1:inorderIndex+1], inorder[:inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex+1:], inorder[inorderIndex+1:])
        
        return root
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        
        
        #Given preorder and inorder traversal of a tree, construct the binary tree.
