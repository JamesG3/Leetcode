# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.stack = []
        self.sum = 0
        
        if not root:
            return 0
        
        self.helper(root)
        return self.sum
        
    def helper(self, node):
        if not (node.left or node.right):
            self.stack.append(str(node.val))
            self.sum += int(''.join(self.stack))
            self.stack.pop()
            return
        
        self.stack.append(str(node.val))
        if node.left:
            self.helper(node.left)
        if node.right:
            self.helper(node.right)
            
        self.stack.pop()
        
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Solution: DFS, leaf detection, stack
Time, Space: O(n)
'''
