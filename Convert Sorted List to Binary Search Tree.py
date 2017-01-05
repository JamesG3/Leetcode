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
    def sortedListToBST(self, head):
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
            
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next        #fast moves with double-speed than slow
            fast = fast.next.next   #when fast reach the tail, slow.next.val is the root of BST
            
        tem = slow.next
        slow.next = None            #divide and conquer
        
        root = TreeNode(tem.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tem.next)
        
        return root
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        #Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
