class Solution(object):
    def summaryRanges(self, nums):
        if(nums==[]):                           #check if nums is empty
            return nums
        
        
        tem=[nums[0]]                           #initializing
        res=[]
        for i in range(1,len(nums)):
            if(nums[i]-nums[i-1]!=1):           
                if(len(tem)==1):
                    res.append("%d"%tem[0])     #single element output situation
                    tem[0]=nums[i]
                    
                else:
                    res.append("%d->%d"%(tem[0],tem[-1]))   #double elements output situation
                    tem=[nums[i]]
            else:                                           #append in res when element is not continuing
                tem.append(nums[i])
                
                
        if(len(tem)==1):                        #output last group of elements
            res.append("%d"%tem[0])
        else:
            res.append("%d->%d"%(tem[0],tem[-1]))
            
        
        return res
        
        
        
  
                    
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Given a sorted integer array without duplicates, return the summary of its ranges.
        # For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]. 
