"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        nlist = [_ for _ in self.traverse(root)]
        
        for i in range(len(nlist)-1):
            l, r = nlist[i], nlist[i+1]
            l.right = r
            r.left = l
        nlist[0].left = nlist[-1]
        nlist[-1].right = nlist[0]
        return nlist[0]
        
        
    def traverse(self, node):
        if not node:
            return
        
        yield from self.traverse(node.left)
        yield node
        yield from self.traverse(node.right)
        
'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

Solution: Traverse, BST, list
Time, Space: O(n)
'''
