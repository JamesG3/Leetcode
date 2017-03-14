class Solution(object):
    def singleNumber(self, nums):
        X = 0
        
        for n in nums:
            X ^= n
        count = 0
        for m in bin(X)[::-1]:
            if m != '1':
                count+=1
            else:
                break
        mark = int('1'+count*'0',2)
        
        a = 0
        b = 0
        for n in nums:
            if n&mark == 0:
                a ^= n
            else:
                b ^= n
        return [a,b]
                
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
        #Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
        
        # XOR all the numbers, the bit with '1' means the difference between two single nnumbers
        # choose a bit with value '1', using this number to distinguish two numbers.
        # XOR all numbers with a certain digit is '1', the result is a
        # XOR all numbers with that certain digit is '0', the result is b
