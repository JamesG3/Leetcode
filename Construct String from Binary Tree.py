# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        global ans
        if t is None:
            return ""
        if t.right is None and t.left is None:
            return str(t.val)
            
        ans = str(t.val)
        ans = ans
        
        self.helper(t.left,1)
        self.helper(t.right, 0)
        return ans
        
    def helper(self, root, mark):
        global ans
        if root == None and mark == 1:
            ans += '()'
            return
        if root == None and mark == 0:
            return
        ans = ans + '(' + str(root.val)
        if root.left or root.right:
            self.helper(root.left, 1)
        
            self.helper(root.right, 0)
        ans = ans + ')'
        
        
        """
        :type t: TreeNode
        :rtype: str
        """
        
        #You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
        #The null node needs to be represented by empty parenthesis pair "()". 
        #And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
        
