class Solution(object):
    def frequencySort(self, s):
        letters = []
        count = []
        ans = ""
        
        for n in s:
            if n not in letters:
                letters += [n]
                count += [1]
            else:
                count[letters.index(n)] += 1
        
        while len(letters) != 0:
            i = count.index(max(count))
            ans += max(count) * letters[i]
            del count[i]
            del letters[i]
            
        return ans
                    
                
            
        """
        :type s: str
        :rtype: str
        """
        
        
        #Given a string, sort it in decreasing order based on the frequency of characters.
