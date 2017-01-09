# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            move = root.left        #save the most left node of the next line temporarily
            while root:             #move the root from left to right, connect all node together
                root.left.next = root.right
                
                if root.next:
                    root.right.next = root.next.left
                root = root.next
            root = move             #set root as the most left node of next line
                    
            
     #Populate each next pointer to point to its next right node. 
     #If there is no next right node, the next pointer should be set to NULL.
     #Initially, all next pointers are set to NULL.
     #You may only use constant extra space.
     #You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
