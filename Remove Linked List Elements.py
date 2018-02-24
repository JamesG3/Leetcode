# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        
        while head and head.val == val:
            head = head.next
        
        if not head:
            return 
        fast, slow = head, head
        
        fast = fast.next
        
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
            
        return head
            
        
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        #Remove all elements from a linked list of integers that have value val
