# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Solution: Tree post order travsersal
        Time: O(n)
        Space: O(logn)
        """
        self.helper(root)
        return root
        
    def helper(self, node):
        if not node:
            return False

        left = self.helper(node.left)
        right = self.helper(node.right)
                
        if not left:
            node.left = None
        if not right:
            node.right = None
        
        return node.val == 1 or left or right
    
    
# Prune children of the tree recursively. The only decisions at each node are whether to prune the left child or the right child.


