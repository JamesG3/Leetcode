# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Solution: Iterative solution using stack
        Time: O(n)
        Space: O(n)
        """
        if not root:
            return res

        res = []
        cur_node = root
        stack = []
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
                
            cur_node = stack.pop()
            res.append(cur_node.val)
            cur_node = cur_node.right
        return res
            
            
        

class Solution(object):
    """
    :type root: TreeNode
    :rtype: List[int]
    Solution: Recursive traversal
    """
    def inorderTraversal(self, root):
        global res
        res=[]
        self.Traversal(root)
        return res
        
    def Traversal(self, root):
        global res
        if root is None:
            return
        self.Traversal(root.left)
        res.append(root.val)
        self.Traversal(root.right)
        
# Given a binary tree, return the inorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?


 
        
