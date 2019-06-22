"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.res = []
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        Solution: Recursive
        Time: O(n)
        """
        if not root:
            return self.res
        self.traversal(root)
        return self.res
        
    def traversal(self, node):
        if not node.children:
            self.res.append(node.val)
            return
        
        for n in node.children:
            self.traversal(n)
        self.res.append(node.val)
            
        
# Given an n-ary tree, return the postorder traversal of its nodes' values.

