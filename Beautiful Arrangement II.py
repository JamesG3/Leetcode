class Solution(object):
    def constructArray(self, n, k):
        ans = range(1, n - k)
        for d in xrange(k+1):
            if d % 2 == 0:
                ans.append(n-k + d/2)
            else:
                ans.append(n - d/2)

        return ans
        
        
        """
    def constructArray(self, n, k):
        ans = range(1, n+1)
        for i in xrange(2, k+1):
            ans = ans[:i-1] + ans[i-1:][::-1]
        return ans
       
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
        # Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
        # Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
        # If there are multiple answers, print any of them.
    
