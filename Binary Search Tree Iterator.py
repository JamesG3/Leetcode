# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:                     #append the left side node in the stack
            self.stack.append(root)
            root = root.left
            
        """
        :type root: TreeNode
        """
        

    def hasNext(self):
        return len(self.stack)!=0
        
        """
        :rtype: bool
        """
        

    def next(self):
        currentnode = self.stack.pop()    #pop the current node
        r = currentnode.right
        while r:                          #append the next several nodes in descending order
            self.stack.append(r)
            r = r.left
        return currentnode.val            #output the current node's val
        
        """
        :rtype: int
        """
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())



#Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#Calling next() will return the next smallest number in the BST.
#Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
