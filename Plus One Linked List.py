# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        Revhead = ListNode(None)
        tmphead = head
        curr = Revhead
        while tmphead:                      # reverse the linked list, new head is Revhead
            Revhead.val = tmphead.val
            tmphead = tmphead.next
            prevNode = ListNode(None)
            prevNode.next = Revhead
            Revhead = prevNode
            
        Revhead = Revhead.next
        tmpRevhead = Revhead
        while tmpRevhead:                   # traverse the reversed linked list, add 1 recursively if needed
            if tmpRevhead.val + 1 == 10:
                if not tmpRevhead.next:
                    tmpRevhead.val = 0
                    last = ListNode(1)
                    tmpRevhead.next = last
                    break
                
                tmpRevhead.val = 0
                tmpRevhead = tmpRevhead.next
                continue
            else:
                tmpRevhead.val += 1
                break
            
        head = ListNode(None)               # reverse the reversed linked list, return the new head
        while Revhead:
            head.val = Revhead.val
            Revhead = Revhead.next
            prevNode = ListNode(None)
            prevNode.next = head
            head = prevNode
        return head.next
            
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
        # You may assume the integer do not contain any leading zero, except the number 0 itself.
        # The digits are stored such that the most significant digit is at the head of the list.
