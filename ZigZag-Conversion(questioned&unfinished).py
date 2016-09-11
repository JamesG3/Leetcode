class Solution(object):
    def convert(self, s, numRows):
        r=""
        row=0
        while(row<numRows-1):
            if (row+3)/2==1:
                n=row
                while((n+(numRows+numRows/2))<len(s)):
                    r+=s[n]
                    n+=numRows+numRows/2
                if row<(numRows-1):
                    row+=1
                else:
                    continue
            if (row+3)/2==0:
                n=row
                while(n+numRows-1 < len(s)):
                    r+=s[n]
                    n+=n+numRows-1
                if row<(numRows-1):
                    row+=1
                else:
                    continue
        return r
                
        """
        :type s: str
        :type numRows: int
        :rtype: str
        what is the answer when row=2 ?
        """
        
