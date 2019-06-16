class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        Enumerate every combination, check if in valid range
        O(1) Time, O(1) Space
        """
        res = []
        rules = {
            1: [0, 9],
            2: [10, 99],
            3: [100, 255]
        }
        length = len(s)
        for i in xrange(1, 4):
            for j in xrange(1, 4):
                for k in xrange(1, 4):
                    for l in xrange(1, 4):                        
                        if (i+j+k+l) != length:
                            continue
                        
                        i1, i2, i3, i4 = int(s[:i]), int(s[i:i+j]), int(s[i+j:i+j+k]), int(s[i+j+k:])
                        
                        if rules[i][0] <= i1 <= rules[i][1]:
                            if rules[j][0] <= i2 <= rules[j][1]:
                                if rules[k][0] <= i3 <= rules[k][1]:
                                    if rules[l][0] <= i4 <= rules[l][1]:
                                        res.append('.'.join([s[:i], s[i:i+j], s[i+j:i+j+k], s[i+k+j:]]))                  
        return res
                    
        
        # Given a string containing only digits, restore it by returning all possible valid IP address combinations.
        # Input: "25525511135"
        # Output: ["255.255.11.135", "255.255.111.35"]

