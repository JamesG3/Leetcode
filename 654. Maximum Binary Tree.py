# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        Solution: Recursive tree construction, DFS
        Time: O(nlgn)
        """
        if not nums:
            return None
        
        cur_max = float('-inf')
        cur_i = 0
        
        for i, n in enumerate(nums):
            if n > cur_max:
                cur_max = n
                cur_i = i
                
        node = TreeNode(cur_max)
        node.left = self.constructMaximumBinaryTree(nums[:cur_i])
        node.right = self.constructMaximumBinaryTree(nums[cur_i+1:])
        
        return node
        
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

