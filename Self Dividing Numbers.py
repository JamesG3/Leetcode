class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        
        for num in xrange(left, right + 1):
            n = num
            flag = 0
            
            while n:
                n, i = divmod(n, 10)
                if i == 0 or num%i:
                    flag = 1
                    break
                    
            if flag == 0:
                res.append(num)
                
        return res
                          
               
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
