class Solution(object):
    def readBinaryWatch(self, num):
        res=[]
        for n in range(0,12):
            for m in range(0,60):
                if bin(n).count('1') + bin(m).count('1') == num:
                    res.append('%d:%02d' % (n, m))
        return res
        
        """
        :type num: int
        :rtype: List[str]
        """
