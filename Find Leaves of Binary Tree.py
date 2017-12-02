# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        if not root:
            return []
        
        global currRes
        res = []
        
        currRes = []
        while self.helper(root):        # repeat untill the last node
            res.append(currRes)         # append current leaves
            currRes = []                # clear current leaves
        res.append(currRes)             # root value
        return res
        
        
    def helper(self, root):             # DFS recursive, delete leaves after each visit
        global currRes
        if not root:
            return
        if not root.left and not root.right:
            currRes.append(root.val)
            return
        else:
            root.left = self.helper(root.left)
            root.right = self.helper(root.right)
            return root


        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

