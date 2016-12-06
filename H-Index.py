class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        length=len(citations)
        if length==0:
            return 0
        elif citations.count(0)==length:
            return 0
        
        for i in range(length):             #method to calculate H-Index
            if citations[i] >= (length-i):
                return length - i
        """
        :type citations: List[int]
        :rtype: int
        """
        
        #For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. 
        #Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.
        
