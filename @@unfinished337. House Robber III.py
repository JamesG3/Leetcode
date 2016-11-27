# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        dic={}
        key=0
        self.helper(root,key,dic)
        sumset=[]
        for n in range(len(dic)):
            sumset.append(dic[n])
            
        sum1=0
        sum2=0
            
            
        ......
        4->1->2->3
        for 4, read 2 and 3, find the larger one to sum, 
        ......
        
        return max(sum1,sum2)
        
        
    def helper(self, root, key, dic):       #recursion, walk the tree, and save the node into dic, using key as index
        if root==None:
            return
        if key in dic:
            dic[key].append(root.val)
        else:
            dic[key]=[root.val]
        self.helper(root.left,key+1,dic)
        self.helper(root.right,key+1,dic)
