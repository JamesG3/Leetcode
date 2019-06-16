class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        Brute force solution
        """
        
        self.roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if not s:
            return 0
        
        res = 0
        cur_str = s[0]
        
        # compare and split the string
        for i in xrange(1, len(s)):
            if self.roman[s[i]] < self.roman[cur_str[-1]]:
                res += self.process(cur_str)
                cur_str = s[i]
            else:
                cur_str += s[i]
                
        res += self.process(cur_str)
        return res
        
    # the string pass to process function is either 'smallBIG' or 'BIG'
    def process(self, cur_str):
        if len(cur_str) > 1 and cur_str[0] != cur_str[-1]:
            small = self.roman[cur_str[0]]
            big = self.roman[cur_str[-1]]
            return cur_str.count(cur_str[-1]) * big - (cur_str.count(cur_str[0]) * small)
        elif cur_str:
            big = self.roman[cur_str[0]]
            return cur_str.count(cur_str[0]) * big 
        else:
            return 0
        
    
    
        """
        :type s: str
        :rtype: int
        Standard Solution
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        if not s:
            return res
        
        for i in xrange(len(s) - 1):
            v = roman[s[i]]
            
            if s[i] == 'I':
                if s[i+1] in set(['V', 'X']):
                    v = -v
            if s[i] == 'X':
                if s[i+1] in set(['L', 'C']):
                    v = -v
            if s[i] == 'C':
                if s[i+1] in set(['D', 'M']):
                    v = -v
                    
            res += v
        res += roman[s[-1]]
        return res
            
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
