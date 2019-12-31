# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tmp_head = TreeNode(None)
        self.head = tmp_head
        self.traverse(root)
        return tmp_head.right
        
        
    def traverse(self, node):
        if not node:
            return None
        self.traverse(node.left)
        self.head.right = node
        node.left = None
        self.head = node
        self.traverse(node.right)
        
'''
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Solution: in-order traverse, BST, tree in-place manipulation
Time: O(n)
Space: O(1)
'''
