class Solution(object):
    # bit solution, O(1)
    class Solution(object):
    def isPowerOfFour(self, num):
        # mask = 1431655765       # using XOR on all power of 4 -> 1010101010101010101010101010101  =  1431655765
        mask = int('0b1010101010101010101010101010101', 2)
        maxx = 2**31
        
        return num > 0 and maxx%num==0 and mask&num == num
    
    
    
    
    # loop & string solution 
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
    
    
    # Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
    # Example:
    # Given num = 16, return true. Given num = 5, return false.
    # Follow up: Could you solve it without loops/recursion?
