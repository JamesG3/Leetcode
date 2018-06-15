# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive solution, O(n) time, O(1) space
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.helper(root, float('-Inf'), float('Inf'))
        
    def helper(self, node, curmin, curmax):
        if not node:
            return True
        if not (curmin < node.val < curmax):
            return False
        return self.helper(node.left, curmin, node.val) and self.helper(node.right, node.val, curmax)

       

# using in-order tree traversal, O(n) time, O(n) space
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
        

        #Given a binary tree, determine if it is a valid binary search tree (BST).
