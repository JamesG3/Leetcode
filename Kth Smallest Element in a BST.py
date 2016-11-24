# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        global res                  #using global varibale to return the final result
        global count                #using global variable, more easy to pass variable between functions
        count=0
        
        self.Traversal(root,k)
        return res
        
    def Traversal(self, root, k):   #in order tree-walk
        global res
        global count
        if root==None:
            return

        if k==count:                    #check if count equals to k before walk to left
            res=root.val
            return
            
        self.Traversal(root.left, k)
        count+=1
        if k==count:
            res=root.val
            return        
        
        self.Traversal(root.right, k)
        
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        #Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
