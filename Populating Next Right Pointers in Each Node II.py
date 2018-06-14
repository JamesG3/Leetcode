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
        node = root
        
        while node:
            dummyNode = TreeLinkNode(0)     # use a dummyNode to relocate the head of each level
            head = dummyNode                # use head as a pointer to help link all nodes in the same level
            while node:
                if node.left:
                    head.next = node.left
                    head = head.next
                if node.right:
                    head.next = node.right
                    head = head.next
                    
                node = node.next            # move to next parent node until end
            
            node = dummyNode.next           # relocate to the head of next level
        
        return
            
                
       # Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
       # Initially, all next pointers are set to NULL. 
       # You may only use constant extra space.
       # Recursive approach is fine, implicit stack space does not count as extra space for this problem.
            
