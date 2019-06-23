# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        Solution: insert from top
        Time: O(nlogn)
        Space: O(n)
        """
        head = TreeNode(preorder[0])
        for val in preorder[1:]:
            self.insert(head, val)
        return head
    
    def insert(self, node, val):
        if val > node.val:
            if node.right:
                self.insert(node.right, val)
            else:
                new_node = TreeNode(val)
                node.right = new_node
                
        else:
            if node.left:
                self.insert(node.left, val)
            else:
                new_node = TreeNode(val)
                node.left = new_node


# Return the root node of a binary search tree that matches the given preorder traversal.
