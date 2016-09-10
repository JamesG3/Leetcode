class Solution(object):
    def reverse(self, x):
        b=list(str(x))
        r=""
        if b[0] == '-':
            r+='-'
            b=b[1:len(b)]
        b.reverse()
        for n in b:
            r+=n
        if -2147483647<int(r)<2147483647:
            return int(r)
        else:
            return 0
            
        """
        :type x: int
        :rtype: int
        """
