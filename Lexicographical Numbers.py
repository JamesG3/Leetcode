class Solution(object):

# one line sort solution, O(nlgn) time
  def lexicalOrder(self, n):
    return sorted(range(1, n+1), key = str)



# DFS solution, TLE
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
    
        self.res = []
        for i in xrange(1, 10):
            self.helper(i, n)
        return self.res
        
        
    def helper(self, i, n):
        if i <= n:
            self.res.append(i)
            j = i*10
            for k in xrange(10):
                self.helper(j+k, n)
        
        
        
        # Given an integer n, return 1 - n in lexicographical order.
        # For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
        # Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
