class Solution(object):
    
    # bit operation solution, O(n) time, O(1) space
    def singleNumber(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
            
        return ans
        
    # math solution, O(2n) time, O(2n) space
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)


        """
        :type nums: List[int]
        :rtype: int
        """
        
