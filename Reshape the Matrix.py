class Solution(object):
    def matrixReshape(self, nums, r, c):
        merge = []
        for l in nums:
            for number in l:
                merge.append(number)
                
        if r*c > len(merge):
            return nums
        
        result = []
        counter = 0
        tem = []
        for n in merge:
            if counter!=0 and float(counter%c) == 0:
                result.append(tem)
                tem = []
                tem.append(n)
            else:
                tem.append(n)
            
            counter+=1
        result.append(tem)
        
        return result
        
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        # You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
        # The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
        # If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

