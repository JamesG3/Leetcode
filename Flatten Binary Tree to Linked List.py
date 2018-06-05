# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1
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

# solution 2
class Solution(object):
    def flatten(self, root):
        if not root:
            return root
        
        node = root
        if node.left:
            tmp = node.right
            node.right = node.left          # move left subtree to right
            node.left = None                # remove left subtree
            self.flatten(node.right)        # flatten recursively
            while node.right:               # get the last right node in current subtree
                node = node.right
            node.right = tmp                # append the original right subtree after the last right node
            self.flatten(node.right)
        else:
            self.flatten(node.right)       
   
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        
        
        #Given a binary tree, flatten it to a linked list in-place.
        #Linked list - only right child

        
