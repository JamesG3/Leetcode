class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic1={}
        dic2={}
        for n in ransomNote:
            if n not in dic1:
                dic1[n]=1
            else:
                dic1[n]+=1
        for m in magazine:
            if m not in dic2:
                dic2[m]=1
            else:
                dic2[m]+=1
        print dic1
        print dic2
        for n in dic1:
            if (n not in dic2) or (dic1[n]>dic2[n]):
                return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
