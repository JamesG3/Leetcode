class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stage_min = [nums[0]]
        for n in nums[1:]:
            if n < stage_min[-1]:
                stage_min.append(n)
            else:
                stage_min.append(stage_min[-1])
        
        # use the stage_minimum list to save 1&3 pattern for each number, 
        # the only thing need to do in the 2nd traversal is comparing with the top of stack to see if it's the 2
        stage_min = stage_min[::-1]
        stack = [nums[-1]]
        for i, n in enumerate(nums[::-1][1:]):
            
            while stack and stage_min[i+1] >= stack[-1]:
                stack.pop()
                
            if stack and n > stack[-1]:
                return True
            stack.append(n)
            
        return False
        
'''
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.

Solution: Stack, traverse and mark
Time, Space: O(n)
'''
            
