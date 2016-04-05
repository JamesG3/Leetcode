class Solution(object):
    def containsDuplicate(self, nums):
        
        #return len(nums) > len(set(nums))                  The fastest solution
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={'index':0}
        for n in nums:
            try:
                print dic[n]
                return True
            except KeyError:
                dic[n]=1
        
        return False
        
        
        #Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. 
        
