# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.root = root
        self.get_depth(self.root)
        
        # binary search on n/2 list
        head, tail = 2**(self.depth - 1), 2**self.depth - 1
        while head <= tail:
            mid = (head + tail) // 2
            if self.if_exist(mid):
                head = mid + 1
            else:
                tail = mid - 1
        return tail
        
        
    def get_depth(self, node):
        self.depth = 0
        while node:
            self.depth += 1
            node = node.left
            
    def if_exist(self, x):
        # use tree features to do a log(n) search
        stack = []
        while x != 1:
            if x%2 == 0:
                stack.append('left')
            else:
                stack.append('right')
            x //= 2
        
        node = self.root
        while stack:
            path = stack.pop()
            if path == 'left':
                node = node.left
            else:
                node = node.right
                
        return node != None
    
'''
Given a complete binary tree, count the number of nodes.
Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Solution: Binary Search, Tree, Data Structure
Time: O(logn ** 2)
Space: O(1)
'''
