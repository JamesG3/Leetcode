class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))    #An simple solution from leetcode
        return r.lstrip('0') or '0'
        
    #    tem=nums[:]                          #my unfished solution, test case like [32,321] could cause wrong answer
    #    res=''                               #still working on it
    #    count=0
    #    while(count<len(tem)):
    #        if(tem[count]>=10):
    #            tem[count]=float(tem[count])/pow(10,len(str(tem[count]/10)))
    #        count+=1
        
        
    #    while(sum(tem)!=-len(tem)):
    #        res+=str(nums[tem.index(max(tem))])
    #        tem[tem.index(max(tem))]=-1
            
    #    return res
    
    
    
    
    #Given a list of non negative integers, arrange them such that they form the largest number.
    #For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
