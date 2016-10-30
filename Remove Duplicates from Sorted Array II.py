class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:                #check boundary value
            return 0
        if len(nums)==1:
            return 1
            
        count=1                         #initialize number counter and index
        index=1
        while index != len(nums):       #read from the second number to the last number
            if nums[index]==nums[index-1]:  #if the former number is same, counter add 1
                count+=1
            else:                       #if different, reset counter to 1
                count=1
            if count>2:                 #if beyond 2 same numbers, delete from the third number
                del nums[index]
                count-=1
                continue
            index+=1
            
        return len(nums)
            
            
            
        """
        :type nums: List[int]
        :rtype: int
        
        Follow up for "Remove Duplicates":
        What if duplicates are allowed at most twice?
        
        For example,
        Given sorted array nums = [1,1,1,2,2,3],
        Your function should return length = 5
        With nums=[1,1,2,2,3]
        """
        
