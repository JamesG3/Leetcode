# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        self.head=head
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        h=self.head
        n=0
        while h!=None:
            h=h.next
            n+=1
        h=self.head
        for i in xrange(random.randrange(0,n)):
            h=h.next
        return h.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
Given a singly linked list, return a random node's value from the linked list. 
Each node must have the same probability of being chosen.

What if the linked list is extremely large and its length is unknown to you? 
Could you solve this efficiently without using extra space?
"""
