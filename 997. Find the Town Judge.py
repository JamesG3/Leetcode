class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusts = {i: 0 for i in range(1, N+1)}
        trusted = {i: set() for i in range(1, N+1)}
        
        for i, j in trust:
            trusts[i] = 1
            trusted[j].add(i)

        for k,v in trusted.items():
            if len(v) == (N-1) and trusts[k] == 0:
                return k
            
        return -1
    
'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Solution: Hashtable
Time, Space: O(n)
'''
