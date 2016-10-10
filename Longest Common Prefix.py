class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[] or "" in strs:
            return ""
        res=strs[0]
        for n in strs[1:]:
                i=0
                j=0
                if n[0] != res[0]:
                    return ""
                while i<len(n) and j<len(res) and n[i]==res[j]:
                    i+=1
                    j+=1
                res=res[:j]
        return res
            
            
        """
        :type strs: List[str]
        :rtype: str
        """
