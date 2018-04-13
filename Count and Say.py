class Solution(object):
    def countAndSay(self, n):
        res = "1"
        
        for _ in xrange(n-1):
            tmp = ''
            num = res[0]
            count = 0
            for n in res:
                if n == num:
                    count += 1
                else:
                    tmp += str(count) + num
                    num = n
                    count = 1
            tmp += str(count) + num
            res = tmp
        return res
            
        
        
        """
        :type n: int
        :rtype: str
        """
        
