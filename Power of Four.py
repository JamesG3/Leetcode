class Solution(object):
    def isPowerOfFour(self, num):
        count=1
        n=bin(int(str(num),10))
        if n.count('1')>1 or num<=0:
            return False
        else:
            while n[-1]!="1":
                n=n[:-1]
                count+=1
                print count
                print n
            if (count-3)%2 == 0:
                return True
            else:
                return False
        """
        :type num: int
        :rtype: bool
        """
        
