# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        if root is None:
            return 0
        
        global sum
        global currentsum
        currentsum = ""             #an empty stack
        sum=0
        self.DFS(root)
        return sum
        """
        :type root: TreeNode
        :rtype: int
        """
        
    def DFS(self, node):
        global sum
        global currentsum
        
        currentsum += str(node.val)                         #stack in
        if node.left is None and node.right is None:        #if leaf, add currensum with sum, then stack out
            sum+=int(currentsum)
            currentsum = currentsum[:-1]
            return
        elif node.left is None:                             #if only right child, traverse right subtree
            self.DFS(node.right)
            currentsum = currentsum[:-1]
        elif node.right is None:                            #if only left child, traverse left subtree
            self.DFS(node.left)
            currentsum = currentsum[:-1]
        else:                                               #if both children, traverse both subtree
            self.DFS(node.left)
            self.DFS(node.right)
            currentsum = currentsum[:-1]                    #stack out
            
            
            
      #Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
      #An example is the root-to-leaf path 1->2->3 which represents the number 123.
      #For example, [1,2,3] returns 25 which is (12+13)
