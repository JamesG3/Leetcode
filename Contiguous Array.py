class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        length = len(nums)
        
        for i in xrange(length):
            if nums[i] == 0:            #build a coordinate, replace the original nums
                count -= 1
            else:
                count += 1
            nums[i] = count
            
        dic = {0:-1}                    #the initial dictionary
        max_len = 0
        for j in xrange(length):        #traverse the coordinate set, if find a new cooridnate, save the cooridnate and index to                                 the dictionary(the new adding one has the minimum index)
            if nums[j] not in dic:
                dic[nums[j]] = j
            else:                       #if the cooridnate already exists, calculate the distance and always pick the larger one
                max_len = max(max_len, j-dic[nums[j]])
                
        return max_len
                
                
                
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        #Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
