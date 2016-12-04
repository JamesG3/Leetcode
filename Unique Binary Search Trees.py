class Solution(object):
    def numTrees(self, n):
                #Catalan Number  (2n)! / ((n+1)! * n!) 
        return math.factorial(2*n) / (math.factorial(n+1)*math.factorial(n))
                
                #recursion solution
        res=[1]
        for i in range(1,n+1):
            tem=0
            for j in range(i):
                tem += res[j] * res[i-j-1]
            res.append(tem)
        return res[-1]
            
        
        """
        :type n: int
        :rtype: int
        """
        
        
        #Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
