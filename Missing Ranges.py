class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        length = len(nums)
        if length == 0:
            if upper - lower == 0:
                res.append(str(upper))    
            elif upper-lower >= 2:
                res.append("->".join([str(lower), str(upper)]))
            return res
        
        left, right = 0, length-1
        
        while nums[left] < lower:
            left += 1
        while nums[right] > upper:
            right -= 1
        nums = [lower-1] + nums[left: right+1] + [upper+1]
        for i in range(1, right-left+3):
            if nums[i] - nums[i-1] <= 1:
                continue
            if nums[i] - nums[i-1] == 2:
                res.append(str(nums[i]-1))
            else:
                res.append("->".join([str(nums[i-1]+1), str(nums[i]-1)]))
                
        
        return res
                
            
  
        
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        
        
        # Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
        # For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
