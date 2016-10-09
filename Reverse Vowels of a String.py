class Solution(object):
    def reverseVowels(self, s):
        Vow="aeiouAEIOU"
        ls=list(s)
        tem=[]
        n=0
        while n!= len(ls):
            if ls[n] in Vow:
                tem.append(ls[n])
                ls[n]="aa"
            n+=1
        m=0
        while len(tem)!=0:
            if ls[m]=="aa":
                ls[m]=tem[-1]
                del tem[-1]
            m+=1
        
        return "".join(ls)
            
                
            
        """
        :type s: str
        :rtype: str
        """
        
