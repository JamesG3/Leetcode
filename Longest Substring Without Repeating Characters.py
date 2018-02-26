class Solution(object):
    # sliding window 2
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i, j, length = 0, 0, len(s)
        mxlen = 0
        
        while j<length:
            if s[j] in dic:
                i = max(i, dic[s[j]])
                
            
            mxlen = max(mxlen, j-i+1)
            dic[s[j]] = j+1
            j += 1
            
        return mxlen
    
    
    # sliding window
    def lengthOfLongestSubstring(self, s):
        st=""
        tem=""
        count=0
        while count<len(s):
            if s[count] not in tem:
                tem+=s[count]
                count+=1
            else:
                if len(tem)>len(st):
                    st=tem
                    tem=tem[tem.find(s[count])+1:]+s[count]
                else:
                   tem=tem[tem.find(s[count])+1:]+s[count]
                count+=1
       
        if len(tem)>len(st):
            return len(tem)
        else:
            return len(st)
                    
                
        """
        :type s: str
        :rtype: int
        Given a string, find the length of the longest substring without repeating characters.
        Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
        """
