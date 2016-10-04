# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root == None:
            return 0
        elif root.left != None and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        
        #set all right leaves equals to 0
        #add all the leaves use recursive
        #because all the right leaves are 0, so the return value would be the sum of all left leaves
        

        
        """
        :type root: TreeNode
        :rtype: int
        Find the sum of all left leaves in a given binary tree.
        """
