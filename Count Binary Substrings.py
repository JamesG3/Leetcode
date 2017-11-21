class Solution(object):
    def countBinarySubstrings(self, s):
        tmpcounter = 1
        Length = len(s)
        rescounter = 0
        counterList = []
        
        for i in xrange(1, Length):
            if s[i] == s[i-1]:
                tmpcounter += 1
            else:
                counterList.append(tmpcounter)
                tmpcounter = 1
        counterList.append(tmpcounter)
        for j in xrange(1, len(counterList)):
            rescounter += min(counterList[j], counterList[j-1])
        return rescounter
                
    
# state machine solution
#     def countBinarySubstrings(self, s):
#         tmpCounter = 1
#         tmpBit = s[0]
#         rescounter = 0
#         Length = len(s)
        
#         if Length == 1:
#             return 0
#         i = 1
#         flag = 1        # increase
#         mark = 0
        
#         while i < Length:
#             if tmpCounter == 0:
#                 i = mark+1
#                 flag = 1
#                 tmpCounter = 1
#                 tmpBit = s[mark]
#                 continue
#             if s[i] == tmpBit:
#                 if flag == 1:
#                     tmpCounter += 1
#                     i += 1
#                 else:
#                     tmpCounter -= 1
#                     rescounter += 1
#                     i += 1
#             else:
#                 if flag == 1:
#                     tmpBit = s[i]
#                     flag = -1
#                     mark = i
#                     tmpCounter -= 1
#                     rescounter += 1
#                     i += 1
#                 else:
#                     i = mark+1
#                     flag = 1
#                     tmpCounter = 1
#                     tmpBit = s[mark]
#                     continue
            
#         return rescounter
        
        
        
# BFS solution (TLE)
#     def countBinarySubstrings(self, s):
#         Length = len(s)
#         global counter
#         counter = 0
#         if Length == 1:
#             return 0
        
#         def bfsHelper(head, tail):
#             global counter
#             if head >= 0 and tail < Length and s[head] != s[tail]:
#                 if tail-head == 1 and s[head] != s[tail]:
#                     counter += 1
#                     bfsHelper(head-1, tail+1)
#                 else:
#                     if s[head]==s[head+1] and s[tail]==s[tail-1]:
#                         counter += 1
#                         bfsHelper(head-1, tail+1)
#             return
                    
#         for i in xrange(Length-1):
#             bfsHelper(i, i+1)
#         return counter
        
        """     
        :type s: str
        :rtype: int
        """
        
        
        # Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
        # Substrings that occur multiple times are counted the number of times they occur.
