# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head
        
        while fast and fast.next:           # find mid point
            slow = slow.next
            fast = fast.next.next
            
        if fast:                    # if odd length, move mid point
            slow = slow.next
            
        tmp1 = None
        
        while slow:             # reverse second part
            tmp2 = slow
            slow = slow.next
            tmp2.next = tmp1
            tmp1 = tmp2
            
        while tmp1:             # compare two parts of the linked list
            if tmp1.val != head.val:
                return False
            tmp1, head = tmp1.next, head.next
            
        return True
        
        
        """
        :type head: ListNode
        :rtype: bool
        """
        # Given a singly linked list, determine if it is a palindrome.
        # Could you do it in O(n) time and O(1) space?

