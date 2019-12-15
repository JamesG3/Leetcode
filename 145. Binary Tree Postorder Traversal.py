# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def postorderTraversal(self, root):
        res=[]
        self.helper(root,res)
        return res
        
        
    def helper(self, root, res):
        if root==None:
            return
        self.helper(root.left,res)
        self.helper(root.right,res)
        res.append(root.val)
       
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        
        if not root:
            return res
        
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
    
    
'''
Given a binary tree, return the postorder traversal of its nodes' values.
Follow up: Recursive solution is trivial, could you do it iteratively?

Solution: Stack / recursive
Get the result of right-first preorder traversal, then reverse the result

Time & Space: O(n)
'''
