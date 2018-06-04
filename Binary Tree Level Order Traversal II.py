# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# stack solution
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        stack = [[root]]
        ans = []
        
        while True:                 # store all node in the order of level
            tmp = stack[-1]
            curlevel = []
            for node in tmp:
                if node.left:
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)
                    
            if not curlevel:
                break
            stack.append(curlevel)
            
        
        while stack:                # read all nodes in reverse order, get value
            curnums = []
            curlevel = stack.pop()
            for node in curlevel:
                curnums.append(node.val)
            ans.append(curnums)
            
        return ans




# in-order traversal solution
class Solution(object):
    def levelOrderBottom(self, root):
        dic={}              #create a dic to save node from every number
        key=0               #using a key to mark the level
        res=[]              #output the dic to res as the final result
        self.helper(root, key, dic)
        for n in range(len(dic)-1,-1,-1):   #output in a reverse sequence
            res.append(dic[n])
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
        :rtype: List[List[int]]
        """
        #Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
        #(ie, from left to right, level by level from leaf to root).
