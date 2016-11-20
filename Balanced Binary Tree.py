# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.maxDepth(root.left)-self.maxDepth(root.right))<2:
            return True             #divide and conquer, must satisfy both subtree is balanced and itself is a balanced tree
        else:
            return False

        
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left) , self.maxDepth(root.right))    #find maxDepth for each node
            


        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #Given a binary tree, determine if it is height-balanced.
        #For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
