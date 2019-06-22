# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        Solution: recursive
        Time: O(logn)
        Space: O(logn)
        """
        self.insert(root, val)
        return root
        
    def insert(self, node, val):
        if node.val > val:
            if node.left:
                self.insert(node.left, val)
            else:
                new_node = TreeNode(val)
                node.left = new_node
        else:
            if node.right:
                self.insert(node.right, val)
            else:
                new_node = TreeNode(val)
                node.right = new_node
                
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. 
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
