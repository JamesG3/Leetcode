# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        fake_head = ListNode('')
        fake_head.next = head
        # the left node, waiting for connection with next avaliable node
        pri = fake_head
        # use this node to traverse the linkedlist
        node = fake_head.next
        occur = 1
        
        while node:
            # find the last node with same value
            while node and node.next and node.val == node.next.val:
                occur += 1
                node = node.next
            
            # if there is nodes with duplicated value, connect this node with pri
            # otherwise, drop this node, go to next node
            if occur == 1:
                pri.next = node
                pri = pri.next
            
            node = node.next
            occur = 1
        
        # to remove the rest of tail with same value
        pri.next = None
        return fake_head.next
                
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Solution: Two pointers, linkedlist operation
Time: O(n)

'''
