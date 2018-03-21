class Solution(object):
    def findStrobogrammatic(self, n):
        dic = {"1":"1", "8":"8", "0":"0", "6":"9", "9":"6"}
        num = [ ["0","0"], ["1","1"], ["6","9"], ["8","8"], ["9","6"]]
        
        if n%2 == 0:
            ans = ['']
        else:
            ans = ['1', '0', '8']
            
        while n>1:
            if n<=3:
                ans = [a + S + b for a,b in num[1:] for S in ans]
            else:
                ans = [a + S + b for a,b in num for S in ans]
            n-=2
        return ans
                
            
            
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        
        # A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
        # Find all strobogrammatic numbers that are of length = n.
        # For example,
        # Given n = 2, return ["11","69","88","96"].
