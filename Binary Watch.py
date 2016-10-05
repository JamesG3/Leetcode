class Solution(object):
    def readBinaryWatch(self, num):
        res=[]
        for n in range(0,12):
            for m in range(0,60):
                if bin(n).count('1') + bin(m).count('1') == num:
                    res.append('%d:%02d'%(n,m))
        return res
        
        
        
        #for every possible situation in [0:00-11:59], judge if it's binary bit sum equals to the num.
        #if equal, append the number of hour and number of minute to the res[] with format "hour:min"
        
        """
        :type num: int
        :rtype: List[str]
        
        A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
        Each LED represents a zero or one, with the least significant bit on the right.
        """
