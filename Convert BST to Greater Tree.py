# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        
        global l
        l = []
        self.traverse(root)
        
        for i in xrange(len(l)-2, -1, -1):
            l[i] += l[i+1]
            
        self.traverse2(root)
        return root
            
    def traverse2(self, root):
        global l
        if root == None:
            return
        self.traverse2(root.left)
        root.val = l[0]
        l = l[1:]
        self.traverse2(root.right)
        
        return
        
        
    def traverse(self, root):
        global l
        if root == None:
            return
        self.traverse(root.left)
        l.append(root.val)
        self.traverse(root.right)
            
        return
        
        
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        #Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
        
        # Or we can use in order tree-walk from right to left to add all nodes
