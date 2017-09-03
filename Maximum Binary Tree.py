# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution(object):                             #recursive DFS 
    def constructMaximumBinaryTree(self, nums):
        R = TreeNode(None)
        self.helper(R, nums)
        return R
        
        
    def helper(self, root, nums):
        if nums == []:
            return None
        M = max(nums)
        mid = nums.index(M)
        root.val = M
        if nums[:mid] != []:
            root.left = TreeNode(None)              #create a new leaf node
            self.helper(root.left, nums[:mid])
        if nums[mid+1:] != []:
            root.right = TreeNode(None)
            self.helper(root.right, nums[mid+1:])
        
        
        
                         
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
        # The root is the maximum number in the array.
        # The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
        # The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
        # Construct the maximum tree by the given array and output the root node of this tree.

