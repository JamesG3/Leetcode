class Solution(object):
    # join list solution, beats 77% solution
    class Solution(object):
    def licenseKeyFormatting(self, S, K):
        
        S = S.replace("-","").upper()
        length = len(S)
        i = length % K
        
        ans = [S[:i]] if i!=0 else []
        
        for j in xrange(length/K):
            ans.append(S[i:i+K])
            i+=K
            
        return "-".join(ans)
        
    
    # brute force, TLE error
    def licenseKeyFormatting(self, S, K):
        tem = S.upper().replace('-','')
        
        #tem = ""
        #for n in S:
        #    if n != '-':
        #        tem += n
        
        S = ""
        index = len(tem)-1
        tem = tem.upper()
        counter = 0
        while index != -1:
            if counter % K == 0 and counter != 0:
                S = '-' + S
            S = tem[index] + S
            index -= 1
            counter+=1
            
        return S
        
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        #Input: S = "2-4A0r7-4k", K = 4
        #Output: "24A0-R74K"
        #Input: S = "2-4A0r7-4k", K = 3
        #Output: "24-A0R-74K"
