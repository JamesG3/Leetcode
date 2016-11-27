# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        dic={}
        key=0
        res=[]
        self.helper(root, key, dic)
        for n in range(len(dic)):       #read the last element in every key's list(right view)
            res.append(dic[n][-1])
        return res
        
        
    def helper(self, root, key, dic):       #recursion, walk the tree, and save the node into dic, using key as index
        if root==None:
            return
        if key in dic:
            dic[key].append(root.val)
        else:
            dic[key]=[root.val]
        self.helper(root.left,key+1,dic)
        self.helper(root.right,key+1,dic)
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #Given a binary tree, imagine yourself standing on the right side of it, 
        #return the values of the nodes you can see ordered from top to bottom.
        
        #For every level, the most right node is what we can see in the right side, so using a dictionary to collect all node's value,
        #Then return the right node from top to bottom
