# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        ahead=head
        behind=head
        
        while behind != None and behind.next != None:       #check if a cycle exists
            ahead=ahead.next
            behind=behind.next.next
            if behind == ahead:
                break
            
        if behind == None or behind.next == None:           #cycle doesn't exist
            return None
            
        ahead = head                #reset ahead
        while ahead != behind:      #seek the cycle node from head
            ahead = ahead.next
            behind = behind.next
        return ahead
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
        #Note: Do not modify the linked list.
        #Can you solve it without using extra space?
