class Solution(object):
    # count element solution O(n * m)
    def groupAnagrams(self, strs):
        dic = {}
        
        for s in strs:
            k = [0 for _ in xrange(26)]
            for c in s:
                k[ord(c) - 97] += 1
            k = tuple(k)
            if k in dic:
                dic[k].append(s)
            else:
                dic[k] = [s]
        return dic.values()
        
    
    
    
    # sort solution, O(n * mlog(m))
    def groupAnagrams(self, strs):
        dic={}
        res=[]
        for n in strs:
            key=''.join(sorted(n)) 
            if key not in dic:          #find key in the dictionary
                dic[key]=[]             #if there isn't key, create one
            dic[key].append(n)          #append current element to the list (using key)
            
        for m in dic:                   #output the result
            res.append(dic[m])
        return res
            
                    
        """
        
        Given an array of strings, group anagrams together.
        For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
        [["ate", "eat","tea"], ["nat","tan"], ["bat"]]
        
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
