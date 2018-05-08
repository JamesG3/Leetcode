class Solution(object):
    # hash set solution (sliding window)
    def containsNearbyDuplicate(self, nums, k):
        length = len(nums)
        s = set()
        
        for i in xrange(length):
            if nums[i] in s:
                    return True
        
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i-k])
                
        return False
    
    
    
    
    
    # dictionary solution
    def containsNearbyDuplicate(self, nums, k):
        dic = {}                              # Init a dictionary,using hash
        tem = 0
        for i in range(0,len(nums)):
            tem = nums[i]
            if (tem not in dic or i-dic[tem] > k):
                dic[tem] = i
            else:
                return True
        return False
            
        
    
#   Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k. 
    
    
    
    
#    def containsNearbyDuplicate(self, nums, k):                    #A time consuming solution
#        if(k==0 or k==len(nums)):
#            return False
#        tem=[]
#        for i in range(0,k):
#            tem.append('index')
#        count=0
#        while(count<len(nums)-1):
            
#            for i in range(0,k):
#                if(nums[count] in tem):
#                    return True
#                else:
#                    tem[i]=nums[count]
#                    count+=1
#                    if(count==len(nums)):
#                        return False
#        return False
            
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
