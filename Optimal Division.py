class Solution(object):
    def optimalDivision(self, nums):
        nums = map(str, nums)
        if len(nums)>2:
            nums[1] = '('+nums[1]
            nums[-1] += ')'
        return '/'.join(nums)
        
        """
        :type nums: List[int]
        :rtype: str
        """
        
        # 1000/(100/10/2) == (1000*10*2)/(100)
        
        # Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.
        # However, you can add any number of parenthesis at any position to change the priority of operations. 
        # You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. 
        # Your expression should NOT contain redundant parenthesis.
