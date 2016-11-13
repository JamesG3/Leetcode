from collections import Counter
#Could be faster if add a condition: if(next letter in s not belongs to p, jump the entire window to the next next letter)
class Solution(object):                     #Sliding window solution
    def findAnagrams(self, s, p):
        ans=[]
        
        S=Counter(s[:len(p)-1])
        P=Counter(p)
        
        for n in range(len(p)-1,len(s)):
            S[s[n]]+=1
            if S == P:
                ans.append(n-len(p)+1)
            S[s[n-len(p)+1]] -= 1
            if S[s[n-len(p)+1]] == 0:
                del S[s[n-len(p)+1]]
        return ans
    
    
        """
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
        Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
        The order of output does not matter.
        
        EXAMPLE:
        Input:
        s: "cbaebabacd" p: "abc"
        Output:
        [0, 6]
        
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
    """
    def findAnagrams(self, s, p):       #brute force solution, check every character and several bits after it
                                        #cause a TLE error
        s=list(s)
        p=list(p)
        index=0
        ans=[]
        
        while index != len(s):

            tem=p[:]
            if s[index] in tem:
                mark=index
                del tem[tem.index(s[index])]
                temi=index+1
                while len(tem) != 0 and temi != len(s):
                    #print mark
                    if s[temi] in tem:
                        del tem[tem.index(s[temi])]
                        temi+=1
                    else:
                        break
            if len(tem) == 0:
                ans.append(mark)
                
            index+=1
                
        return ans
        

        """
