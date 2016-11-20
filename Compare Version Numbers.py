class Solution(object):
    def compareVersion(self, version1, version2):
        v1=version1.split('.')          #compare version1 and version2 part by part, from left to right
        v2=version2.split('.')
        
        l1=len(v1)
        l2=len(v2)
        minlen=min(l1,l2)               #the length of overlapping parts
        
        for i in range(minlen):         #compare overlapping parts
            if int(v1[i])<int(v2[i]):
                return -1
            if int(v1[i])>int(v2[i]):
                return 1
                                        #if we are here, means the overlapping parts are same
        if l1<l2:                       #for the longer version, if there is one digit which is not 0, it's larger
            for i in range(minlen,l2):
                if int(v2[i])!=0:
                    return -1

        if l1>l2:
            for i in range(minlen,l1):
                if int(v1[i])!=0:
                    return 1
        return 0                        #all digits are 0, means the two versions are equal
        
        
        """
        
        Compare two version numbers version1 and version2.
        If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
        You may assume that the version strings are non-empty and contain only digits and the . character.
        The '.' character does not represent a decimal point and is used to separate number sequences.
        
        For instance, 2.5 is not "two and a half" or "half way to version three", 
        it is the fifth second-level revision of the second first-level revision.
        
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
