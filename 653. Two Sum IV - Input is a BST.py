# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        l = []
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            l.append(node.val)
            helper(node.right)
            
        helper(root)
        i, j = 0, len(l) - 1
        
        while i < j:
            s = l[i] + l[j]
            if s < k:
                i += 1
            elif s > k:
                j -= 1
            else:
                return True
            
        return False
        
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        # Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
