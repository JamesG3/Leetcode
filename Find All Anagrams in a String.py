class Solution(object):
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
       
        :type s: str
        :type p: str
        :rtype: List[int]
        """
