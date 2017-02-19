class Solution(object):
    def nextGreaterElements(self, nums):
        length = len(nums)
        res = [-1]*length           #initialize a list with len*[-1]
        stack = []                  #a stack for saving index
        
        for index, i in enumerate(nums*2):      #for every number and it's index
            while stack and i>nums[stack[-1]]:  #if stack is not empty, compare the last number with the current number i
                res[stack.pop()] = i            #update the value in res until find a number larger than current number
            if index<length:                    #push the current index into stack
                stack.append(index)
                
        return res
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #Given a circular array (the next element of the last element is the first element of the array), 
        #print the Next Greater Number for every element. 
        #The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. 
        #If it doesn't exist, output -1 for this number.
