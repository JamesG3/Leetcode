# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # solve edge cases here
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        
        ledge, redge, self.leaves = [], [], []
        self.traverse(root)
        
        # get left edge
        node = root.left
        while node:
            if node.left:
                ledge.append(node.val)
                node = node.left
            elif node.right:
                ledge.append(node.val)
                node = node.right
            else:
                node = None
            
        # get right edge
        node = root.right
        while node:
            if node.right:
                redge.append(node.val)
                node = node.right
            elif node.left:
                redge.append(node.val)
                node = node.left
            else:
                node = None
        
        return [root.val] + ledge + self.leaves + redge[::-1]
    
    # get all leaves
    def traverse(self, node):
        if not node:
            return
        
        l = self.traverse(node.left)            
        r = self.traverse(node.right)
        if not r and not l:
            self.leaves.append(node.val)
        
        return True
        
        
'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Solution: Divide and conquer, tree traversal
Time: O(n)
'''
