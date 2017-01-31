# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tree traversal solution:
class Solution(object):
    def findMode(self, root):
        dic={}
        self.treewalk(root, dic)    #get the count of all numbers in the tree
        ans = []
        tem = -1                #set tem as an enough small number
        for n in dic:
            if dic[n]>tem:      #always update to a larger number
                ans=[n]         #reset ans
                tem = dic[n]    #update tem to the larger number
                continue
            
            elif dic[n]==tem:
                ans.append(n)
        return ans
                
        
        
    def treewalk(self, root, dic):       #in-order traverse
        if root is None:
            return
        self.treewalk(root.left, dic)
        if root.val not in dic:             #save the count of the current number
            dic[root.val] = 1
        else:
            dic[root.val] += 1
        self.treewalk(root.right, dic)
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        #Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
        #
