# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        res=[]
        self.currentlevel(root, 0, res)
        return res
        
        
    def currentlevel(self, root, level, res):     #for every level, append new number to it's corresponding list
        if root != None:
            if len(res)<level+1:                #if not leave, create a new empty list
                res.append([])                  #then append current number to that list
            res[level].append(root.val)
            self.currentlevel(root.left, level+1, res)    #recurrence with level+1
            self.currentlevel(root.right, level+1, res)
        
        """
        
        Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
        For example:
        Given binary tree [3,9,20,null,null,15,7],
        return [[3],[9,20],[15,7]]
        
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
