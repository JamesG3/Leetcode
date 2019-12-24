class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length < 10:
            return []
        
        res_set = set([])
        l, r = 0, 10
        tmp_s = ''.join([s[i] for i in range(l, r)])
        dna_pat = set([tmp_s])
        
        for j in range(length - 10):
            tmp_s = tmp_s[1:] + s[r + j]
            if tmp_s not in dna_pat:
                dna_pat.add(tmp_s)
            else:
                res_set.add(tmp_s)
            
        return list(res_set)
    
    
'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Solution: hashtable, traverse all patterns in the DNA string
Time: O(n)
Space: O(n)
'''
