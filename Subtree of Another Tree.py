# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# subtree compare solution, O(n*m) time and O(n) space
class Solution(object):
    def isSubtree(self, s, t):
    
        def compare(t1, t2):
            if not t1 and not t2:
                return True
            elif (t1==None or t2==None):
                return False
            return (t1.val == t2.val and compare(t1.left, t2.left) and compare(t1.right, t2.right))
        
        def traverse(s, t):
            return s is not None and (compare(s, t) or traverse(s.left, t) or traverse(s.right, t))
        
        return traverse(s, t)


# tree traversal solution, string solution
class Solution(object):

    def isSubtree(self, s, t):
        global Tem
        Tem = ""
        
        self.helper(s)
        S = Tem
        
        Tem = ""
        self.helper(t)
        T = Tem

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
