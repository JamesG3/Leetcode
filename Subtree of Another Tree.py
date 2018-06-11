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


# string solution, pre-order traversal, super fast!
class Solution(object):
    def __init__(self):
        self.s_str = ""
        self.tmp = ""
    
    def isSubtree(self, s, t):
        self.traversal(s)
        self.s_str = self.tmp
        self.tmp = ""
        self.traversal(t)
        # print self.tmp, self.s_str
        return self.tmp in self.s_str
        
    def traversal(self, node):
        if not node:
            self.tmp += " "
            return
        self.tmp += "*" + str(node.val)     # add a special character before each node
        self.traversal(node.left)           # pre-order traversal works!
        self.traversal(node.right)
        
        
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. 
        # The tree s could also be considered as a subtree of itself.
