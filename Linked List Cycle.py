# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        ahead=head
        behind=head
        
        while behind != None and behind.next != None:
            ahead=ahead.next
            behind=behind.next.next
            if behind == ahead:
                return True
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        
