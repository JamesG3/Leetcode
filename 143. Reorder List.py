# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.par = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        node = head
        par = None
        while node.next:
            node.par = par
            par = node
            node = node.next
        node.par = par
        
        end = node
        node = head
        
        while node:
            next_node = node.next
            if next_node == end:
                break
                
            # stop breaking link for the very last node (when length is odd)
            if next_node:
                end.par.next = None
                node.next = end
                end.next = next_node
            node = next_node
            end = end.par
        
        return head
                
'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

Solution: Linked List, parent, order, in-place
Time: O(n)
Space: O(1)

'''       
        
        
        
