class Solution(object):
    def numWays(self, n, k):
        if not n or not k:
            return 0
        if n==1:
            return k
        
        same = k
        diff = k*(k-1)
        
        for i in xrange(3, n+1):
            same, diff = diff, (same+diff)*(k-1)        # same = p(previous is diff)
        return same + diff

        
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        # There is a fence with n posts, each post can be painted with one of the k colors.
        # You have to paint all the posts such that no more than two adjacent fence posts have the same color.
        # Return the total number of ways you can paint the fence.
