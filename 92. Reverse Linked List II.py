# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        reverse_head = None
        pri_reverse = None
        left_head = None
        node = head
        
        # make sure the node will reach and reverse the Nth node
        for i in range(n):
            # prepare the nxt node
            nxt = node.next
            
            # if m found, save the first node as the left_head, for future use
            if m == 1:
                reverse_head = node
                left_head = node
            
            # for the rest of nodes, move each node as the current new head
            elif m < 1:
                node.next = reverse_head
                reverse_head = node
            
            # find the node right before left_head (node m)
            else:
                pri_reverse = node
            
            node = nxt    
            m -= 1
        
        # build the connection between orig_left_head to the rest of linkedlist
        left_head.next = node
        
        # if m == 1, then the reversed head itself is the current new head
        if not pri_reverse:
            return reverse_head
        # else, build the connection between pri_reverse head and the current reversed head
        else:
            pri_reverse.next = reverse_head
            return head
'''
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Solution: LinkedList operation, in place, two(more) pointers
Time: O(n)
Space: O(1)
'''
