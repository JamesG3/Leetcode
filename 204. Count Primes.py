class Solution(object):
    def countPrimes(self, n):
        nums = range(2,n)
        count=0
        
        def Eratosthenes(nums, n, i):
            LEN=len(nums)
            index=i+n
            while index<LEN:                #set all multiples of prime n to negative
                if nums[index]>0:
                    nums[index] = -nums[index]
                index+=n

        
        for i in xrange(n-2):   #if the current number is a prime number, using Eratosthenes to modify nums
            if nums[i]>0:
                count+=1
                Eratosthenes(nums,nums[i],i)
        
            
        return count
        
        
        
        """
# this solution will be a bit faster
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [1] * n
        res[0] = res[1] = 0
        
        for i in xrange(2, n):
            if res[i] == 1:
                for j in xrange(2, (n-1)//i+1):
                    res[i*j] = 0
                    
        return sum(res)
        
        """
        
        #Count the number of prime numbers less than a non-negative number, n.
        #The Sieve of Eratosthenes is one of the most efficient ways to find all prime numbers up to n.
