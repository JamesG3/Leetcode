# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.itator = self.traverse(root)
        try:
            self.cur = self.itator.__next__()
        except:
            self.cur = None

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur = self.cur
        try:
            self.cur = self.itator.__next__()
        except:
            self.cur = None
        return cur
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur != None
            
        
    def traverse(self, node):
        if not node:
            return
        
        yield from self.traverse(node.left)
        yield node.val
        yield from self.traverse(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

Solution: Tree traversal, BST, generator
Time: O(1) avg
Space: O(h) Memory
'''
