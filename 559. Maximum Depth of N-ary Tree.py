"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.res = 0
        self.dfs(root, 1)
        return self.res
        
    def dfs(self, node, depth):
        if not node:
            return
        
        self.res = max(self.res, depth)
        for n in node.children:
            self.dfs(n, depth+1)
            
'''
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Solution: DFS, recursive
Time: O(n)
Space: O(1)
'''
