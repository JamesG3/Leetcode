class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        #in O(n) time and no extra space:
        length=len(nums)
        for i in range(length):         #revalue every number, mark all existing number
            index = abs(nums[i])-1      #find the index of all existing numbers (increasing sequence)
            nums[index] = -abs(nums[index]) #set every corresponding number of every existing number to negative
            
        
        res=[]
        for i in range(length):         #read every number again to find out which index belongs to those disappeared nubmers
            if nums[i]>0:               #add every missing number to result
                res.append(i+1)
        return res
            
            
        
        """
        #brute force
        #when the nums getting larger enough, searching wastes lots of time
        
        length=len(nums)
        res=[]
        for i in range(1,length+1):
            if i not in nums:
                res.append(i)
                
        return res
        
        
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        #Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        #Find all the elements of [1, n] inclusive that do not appear in this array.
        #Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
