# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # solution: recursive, need more time
#     def sortedListToBST(self, head):
#         if head is None:
#             return
#         if head.next is None:
#             return TreeNode(head.val)
            
#         slow = head
#         fast = head.next.next
        
#         while fast and fast.next:
#             slow = slow.next        #fast moves with double-speed than slow
#             fast = fast.next.next   #when fast reach the tail, slow.next.val is the root of BST
            
#         tem = slow.next
#         slow.next = None            #divide and conquer
        
#         root = TreeNode(tem.val)
#         root.left = self.sortedListToBST(head)
#         root.right = self.sortedListToBST(tem.next)
        
#         return root


    def sortedListToBST(self, head: ListNode) -> TreeNode:
        length = 0
        tmp_head = head
        while tmp_head:
            length += 1
            tmp_head = tmp_head.next
        self.head = head
        return self.in_order(0, length)
        
            
    def in_order(self, l, r):
        if l >= r:
            return None
        
        mid = (l + r) // 2
        left_node = self.in_order(l, mid)
        
        cur_node = TreeNode(self.head.val)
        self.head = self.head.next
        cur_node.left = left_node
        
        right_node = self.in_order(mid+1, r)
        
        cur_node.right = right_node
        return cur_node
    
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

This is a awesome solution!!
    1st linkedlist traversal -> get the length of list, so we'll know the BST size(depth)
    in order traverse (create) the BST, assign value while traversing the linkedlist again.
Time: O(n)
Space: O(n), extra O(logn)
'''
