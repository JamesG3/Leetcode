# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder = postorder
        self.index_map = {v:i for i,v in enumerate(inorder)}
        
        res_node = self.build(0, len(inorder) - 1)
        return res_node
    
    
    def build(self, left, right):
        if left > right:
            return None
        
        cur_val = self.postorder.pop()
        node = TreeNode(cur_val)
        i = self.index_map[cur_val]
        node.right = self.build(i+1, right)
        node.left = self.build(left, i-1)
        
        return node

'''
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

Solution: 
- Use postorder to find the parent node one by one (from root, right-first in-order traverse)
- Split inorder into two parts, recursivly traverse right and left subtree

Time: O(n)
Space: O(n)
''' 
