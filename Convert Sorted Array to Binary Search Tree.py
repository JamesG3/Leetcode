# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        
        mid = len(nums) / 2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        #Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
                
