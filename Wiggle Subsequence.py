class Solution(object):
    def wiggleMaxLength(self, nums):
        length = len(nums)
        if length < 2:
            return length
        
        count = 1
        index = 1
        while index != length:
            if nums[index] != nums[index-1]:    #jump the first several duplicate numbers
                break
            index+=1
            
        if index == length:     #if all numbers are same
            return count
        else:
            count+=1
        
        if nums[index-1] < nums[index]:
            direction = 1           #increase is the initial direction
        elif nums[index-1] > nums[index]:
            direction = 0           #decrease is the initial direction
        tem = nums[1]
 
        for i in xrange(index, len(nums)):
            if direction == 1:      #if current direction is increase
                if nums[i] >= tem:
                    tem = max(nums[i], tem)
                
                else:
                    direction = 0   #set next expected direction to decrease
                    tem = nums[i]
                    count+=1
                    
            else:                   #if current direction is decrease
                if nums[i] <= tem: 
                    tem = min(nums[i], tem)
                else:
                    direction = 1   #set next expected direction to increase
                    tem = nums[i]
                    count+=1
                
        return count
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
        #The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
        #return the length of the longest subsequence that is a wiggle sequence. 
