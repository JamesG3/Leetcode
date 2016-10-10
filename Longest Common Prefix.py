class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[] or "" in strs:                  #return empty string in these situation
            return ""
        res=strs[0]
        for n in strs[1:]:                          #use the first element for initial res, and compare with each element in the array.
                i=0
                j=0
                if n[0] != res[0]:                  #return empty string if the first character is different
                    return ""
                while i<len(n) and j<len(res) and n[i]==res[j]:
                    i+=1
                    j+=1
                res=res[:j]                         #update the res
        return res
            
            
        """
        :type strs: List[str]
        :rtype: str
        
        Write a function to find the longest common prefix string amongst an array of strings.
        """
