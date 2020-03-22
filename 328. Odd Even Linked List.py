# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        h, t = head, head.next
        while t and t.next:
            h_nxt = h.next
            t_nxt = t.next
            
            t.next = t.next.next
            h.next = t_nxt
            t_nxt.next = h_nxt
            h = t_nxt
            t = t.next
        
        return head
            
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Solution: linked list in-place operation
Time: O(n)
Space: O(1)
'''
