# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Recursive solution
    def preorderTraversal(self, root):
        res=[]
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root==None:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
        

class Solution:
    # Recursive (Stack) solution
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        if not root:
            return res
        
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
'''
Given a binary tree, return the preorder traversal of its nodes' values.
Follow up: Recursive solution is trivial, could you do it iteratively?

Solution: Stack / recursive
Time & Space: O(n)
'''
