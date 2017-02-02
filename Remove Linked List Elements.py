# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        while head is not None and head.val == val:     #remove the first several elements
            head = head.next
        if head is None:                #if the LinkList is empty, return head
            return head
            
        fast = head.next                #if not Empty, set a fast and a slow pointer
        slow = head
        
        while fast != None:             #traverse the Linklist and remove all the elements have value val
            if fast.val == val:
                fast = fast.next
                slow.next = slow.next.next
            else:
                fast = fast.next
                slow = slow.next
        return head
            
        
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        #Remove all elements from a linked list of integers that have value val
