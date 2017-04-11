class Solution(object):
    def nextGreaterElement(self, n):
        N = list(str(n))
        if len(N) == 1:
            return -1
        
        dic = {}                                # use a dic to save number and it's index
        mark = 0
        for i in xrange(len(N)- 1,0,-1):            #read from the last digit
            if int(N[i]) not in dic:                #save each number into dic, if duplicate, choose the left most digit
                dic[int(N[i])] = i
            else:
                dic[int(N[i])] = i
                
            if int(N[i]) > int(N[i-1]):         # stop saving number into dic when decreasing
                M = max(dic)                    # initialize the minimum number
                for n in dic:   # for numbers in dic, find the minimum number which larger than N[i-1] and smaller than N[i]
                    if int(N[i-1]) < n < int(N[i]):
                        M = min(M, n)
                        
                N[i-1], N[dic[M]] = N[dic[M]], N[i-1]   # switch the two numbers
                mark = 1
                N = N[:i] + sorted(N[i:])               # sort the number after N[i], (the next greater element)
                break
        if mark == 1 and int(''.join(N)) < 2147483648: 
            return int(''.join(N))
        
        else:
            return -1
                        
                        
                        
        """
        :type n: int
        :rtype: int
        """
        #Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. 
        #If no such positive 32-bit integer exists, you need to return -1.
