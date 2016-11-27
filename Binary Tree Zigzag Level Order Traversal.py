# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        
        dic={}
        key=0
        self.helper(root, key, dic)
        res=[]
        
        for n in range(len(dic)):
            if n%2 != 0:                    #read the dic in order or in reverse order based on odd or even key
                res.append(dic[n][::-1])
            else:
                res.append(dic[n])
        
        return res
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        
        
    def helper(self, root, key, dic):       #recursion, walk the tree, and save the node into dic, using key as index
        if root==None:
            return
        if key in dic:
            dic[key].append(root.val)
        else:
            dic[key]=[root.val]
        self.helper(root.left,key+1,dic)
        self.helper(root.right,key+1,dic)
        
        
        
        
        #Given a binary tree, return the zigzag level order traversal of its nodes' values. 
        #(ie, from left to right, then right to left for the next level and alternate between).
        #Given binary tree [3,9,20,null,null,15,7],
        #return [[3], [20,9], [15,7]]
        
