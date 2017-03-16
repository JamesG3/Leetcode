# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):            # Solution1: Add two number first and crate the ans Linked list
        num1 = 0
        num2 = 0
        
        if l1 is not None:
            while l1:
                num1 = num1*10 + l1.val
                l1 = l1.next
        if l2 is not None:
            while l2:
                num2 = num2*10 + l2.val
                l2 = l2.next
        
        SUM = str(num1 + num2)
        tem = None
        for n in xrange(len(SUM)-1,-1,-1):
            ans = ListNode(int(SUM[n]))
            ans.next = tem
            tem = ans
        return ans
            
        
        
    def addTwoNumbers(self, l1, l2):              # Solution2: Using two stacks to sump up two linked lists
        stack1 = []
        stack2 = []
        
        head1 = l1
        head2 = l2
        
        while head1 != None:
            stack1.append(head1.val)
            head1 = head1.next
        while head2 != None:
            stack2.append(head2.val)
            head2 = head2.next
        
        add = 0
        tem = None
        while len(stack1)!=0 and len(stack2)!=0:
            SUM = stack1.pop()+stack2.pop()+add
            if SUM >= 10:
                add = 1
                SUM = SUM%10
            else:
                add = 0
            ans = ListNode(SUM)
            ans.next = tem
            tem = ans
        
        reststack = []                  # sum up the rest part
        if len(stack1)!=0:
            reststack = stack1
        elif len(stack2)!=0:
            reststack = stack2
            
        while len(reststack)!=0:
            SUM = reststack.pop()+add
            if SUM >= 10:
                add = 1
                SUM = SUM%10
            else:
                add = 0
            ans = ListNode(SUM)
            ans.next = tem
            tem = ans
            
        if add == 1:                    # sum up the last digit
            ans = ListNode(1)
            ans.next = tem
        
        return ans
            
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        # You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        # You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        # What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
        # Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        # Output: 7 -> 8 -> 0 -> 7
        
