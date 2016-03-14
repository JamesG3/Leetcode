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
        
        
