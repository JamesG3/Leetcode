"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        # if has right child, then successor must be in right subtree
        if node.right:
            succ = node.right
            while succ and succ.left:
                succ = succ.left
            return succ
        
        parent = node
        has_par = False
        # find the parent until find the parent of current left subtree
        # if there is no such parent, means there is no successor
        while node.parent:
            if not node.parent.left == node:
                node = node.parent
            else:
                par = node.parent
                has_par = True
                break
        if not has_par:
            return None
        return par
        
'''
Given a node in a binary search tree, find the in-order successor of that node in the BST.
If that node has no in-order successor, return null.
The successor of a node is the node with the smallest key greater than node.val.
You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node

Solution: Tree operation
Time: O(logn)
Space: O(1)
'''
