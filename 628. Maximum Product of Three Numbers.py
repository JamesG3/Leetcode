# O(n) time, O(1) space solution
class Solution(object):
    def maximumProduct(self, nums):
        length = len(nums)
        if length < 3:
            return 0
        
        # traverse once, store the minimum 2 numbers and 3 maximum numbers
        # compare the products
        
        min1, min2 = float('Inf'), float('Inf')
        max1, max2, max3 = float('-Inf'), float('-Inf'), float('-Inf')
        
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
                
        return max(min1 * min2 * max1, max1 * max2 * max3)
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # Given an integer array, find three numbers whose product is maximum and output the maximum product.

