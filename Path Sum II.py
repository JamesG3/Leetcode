# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.S = sum
        if not root:
            return []
        
        self.helper(root, 0, [])
        return self.res
        
        
    def helper(self, node, cursum, curpath):
        if not node.left and not node.right:
            if cursum+node.val == self.S:
                self.res.append(curpath+[node.val])
            return
        
        if node.left:
            self.helper(node.left, cursum+node.val, curpath+[node.val])
        if node.right:
            self.helper(node.right, cursum+node.val, curpath+[node.val])
                
                
                
    # Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    # Note: A leaf is a node with no children.
