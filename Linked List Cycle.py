# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        ahead=head
        behind=head
        
        while ahead != None and ahead.next != None:             #if the one goes ahead reach the end of list, break and return False
            behind=behind.next
            ahead=ahead.next.next
            if behind == ahead:                                 #go on until ahead meet behind                     
                return True
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        
