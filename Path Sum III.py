# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n^2) time solution
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.counter = 0
        self.helper(root, sum)
        return self.counter

    def helper(self, node, target):
        if not node:
            return
        
        self.test(node, target)             # any traverse order is OK!
        self.helper(node.left, target)
        self.helper(node.right, target)
        
    def test(self, node, target):
        if not node:
            return
        if node.val == target:
            self.counter += 1
            
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
        
         
        
        
        # You are given a binary tree in which each node contains an integer value.
        # Find the number of paths that sum to a given value.
        # The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
        # The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
