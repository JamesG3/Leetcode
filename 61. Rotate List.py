# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
            
        length = 0
        tmp_head = head
        old_tail = None
                        
        while tmp_head:
            if not tmp_head.next:
                old_tail = tmp_head
            length += 1
            tmp_head = tmp_head.next
            
        actual_step = k % length
        if actual_step == 0:
            return head
        
        shft_pnt = length - 1 - actual_step
        counter = 0
        tmp_head = head
        
        while counter != shft_pnt:
            counter += 1
            tmp_head = tmp_head.next
            
        new_head = tmp_head.next
        tmp_head.next = None
        old_tail.next = head
        return new_head
        
'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Solution: Linked List operation, two pointers
Time & Space: O(n)
'''
