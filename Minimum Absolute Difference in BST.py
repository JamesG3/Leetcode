# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        global L
        L = []
        self.helper(root)           #get all nodes' value
        
        L.sort()                    #sort in increasing order
        MIN = L[1]-L[0]             #initialize the MIN value
        for i in xrange(1, len(L)-1):       #always choose the smaller one
            MIN = min(MIN, L[i+1]-L[i])
        
        return MIN
        
        
    def helper(self, root):         #Traverse all the nodes
        global L
        if root is None:
            return
        self.helper(root.left)
        L.append(root.val)
        self.helper(root.right)
        
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        #Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
