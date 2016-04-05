# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while (left<right):
            mid = (left+right)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
        """
        :type n: int
        :rtype: int
        """
        
        # You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
        # Since each version is developed based on the previous version, all the versions after a bad version are also bad.

        # Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. 
        
