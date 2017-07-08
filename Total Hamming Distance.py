class Solution(object):
    def totalHammingDistance(self, nums):
        total = 0
        length = len(nums)
        for i in xrange(32):
            count_1 = sum([m>>i & 1 for m in nums])     #for each same digit for all the numbers, count the appearance of 1
            total += count_1*(length-count_1)      #total hamming distance for each digit = (appearance of 1) * (appearance of 0)
        return total
        
        """
        total = 0
        length = len(nums)
        
        for i in xrange(length):
            for j in xrange(i+1, length):
                total += bin(nums[i]^nums[j]).count('1')
        return total
        
        
        :type nums: List[int]
        :rtype: int
        """
        # The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
        # Now your job is to find the total Hamming distance between all pairs of the given numbers.
