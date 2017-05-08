# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        global Tem
        Tem = ""
        
        self.helper(s)
        S = Tem
        
        Tem = ""
        self.helper(t)
        T = Tem
        
        print S
        print T
        return T in S
        
        
        
    def helper(self, root):
        global Tem
        if root is None:
            Tem += "n"
        
        else:
            Tem+=str(root.val)
            self.helper(root.left)
            self.helper(root.right)
        
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. 
        # The tree s could also be considered as a subtree of itself.
