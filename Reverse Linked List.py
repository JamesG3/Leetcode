# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        
        count=None
        while head:
            tem=head
            head=head.next
            tem.next=count
            count=tem
            
        return count
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
