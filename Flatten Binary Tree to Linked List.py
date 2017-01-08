# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.current = None             #a global variable to save the current node
    
    def flatten(self, root):
        if root is None:
            return
        
        self.flatten(root.right)        #reverse pre-order traversal(not post order!)
        self.flatten(root.left)
        

        root.right = self.current       #set the last visit node as the right child of the current node
        root.left = None
        self.current = root             #update self.current to current node

        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        #Given a binary tree, flatten it to a linked list in-place.
        #Linked list - only right child
