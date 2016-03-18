class Solution(object):
    def romanToInt(self, s):
        count=0
        Dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Sum=Dic[s[0]]
        
        while(count<len(s)-1):
            if(Dic[s[count]]<Dic[s[count+1]]):
                Sum+=Dic[s[count+1]]-2*Dic[s[count]]
            else:
                Sum+=Dic[s[count+1]]
            count+=1
        return Sum
        """
        :type s: str
        :rtype: int
        """
