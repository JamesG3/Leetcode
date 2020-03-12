from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if length * k == 0:
            return []
        if k == 1:
            return nums
        
        # use deque data structure to support O(1) pop from top and bottom
        deq = deque()
        mx_i = 0
        res = []
        
        # use this function to update deque
        # age out the element outside the sliding window
        # only keep all the elements larger than current element, which mean the element inside queue is in ASC order
        # the bottom of the queue is the local maximum
        def update_q(i):
            if deq and i - deq[0] == k:
                deq.popleft()
                
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
        
        # init the queue and cur_max
        for i in range(k):
            update_q(i)
            deq.append(i)
            if nums[i] >= nums[mx_i]:
                mx_i = i
        res.append(nums[mx_i])
        
        # process the rest
        for i in range(k, length):
            update_q(i)
            deq.append(i)
            res.append(nums[deq[0]])
            
        return res
            
            
'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Solution: Use queue, deque, support O(1) time to pop from both head and tail, data structure, greedy
Time: O(n)
Space: O(n)
'''
            
        
        
