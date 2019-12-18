# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smal = smal_head = ListNode(0)
        big = big_head = ListNode(0)
        
        while head:
            if head.val >= x:
                big_head.next = head
                big_head = big_head.next
            else:
                smal_head.next = head
                smal_head = smal_head.next
            head = head.next
            
        # break the loop in linked list
        big_head.next = None
        smal_head.next = big.next
        return smal.next
                

                
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Solution: create two linkedlist to re-organize the orig linked list
Time: O(n)
Space: Extra O(1)
'''
