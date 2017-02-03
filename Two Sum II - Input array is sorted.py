class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        
        while left < right:           #add two numbers(one starts from end, one from start)
            sum = numbers[left]+numbers[right]
            if sum > target:          #if larger, change a smaller number then add again
                right -= 1
            elif sum < target:        #if smaller, change a larger number
                left += 1
            else:
                return [left+1,right+1]
        return [-1,-1]
                
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
