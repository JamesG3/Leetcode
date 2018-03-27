class Solution(object):
    
    # BFS
    def numSquares(self, n):
        if n<2:
            return n
        
        sqr = []
        for i in xrange(1, int(math.sqrt(n))+1):
            sqr.append(i**2)
            
        res = 0
        dic = {n}
                                        # BFS, using set to store all possible numbers after minus each perfect square number
        while dic:                      # repeat until a perfect square number appears in the dic
            res+=1
            tmp = set()
            for x in dic:
                for y in sqr:
                    if x == y:
                        return res
                    if x < y:
                        break
                    tmp.add(x-y)
                dic = tmp
        return res
       
        
        """
        :type n: int
        :rtype: int
        """
        
        # Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

        # For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. 
