class Solution(object):
    def findDiagonalOrder(self, matrix):
        i = 0
        j = 0
        
        if len(matrix) == 0:
            return []
        
        M = len(matrix[0])
        N = len(matrix)
        
        if M == 1 and N != 1:
            ans = []
            for n in matrix:
                ans+=n
            return ans
        elif M != 1 and N == 1:
            return matrix[0]
        
        mark = 0
        ans = []
        
        
        while i+j != M+N-2:
            ans.append(matrix[i][j])
            if mark == 0 and j+1<M:
                j += 1
                mark = 1
            elif mark == 1:
                if j!=0 and i!=N-1:
                    j-=1
                    i+=1
                elif j==0 and i==N-1:
                    j += 1
                    mark = 2
                elif j!=0 and i==N-1:
                    j+=1
                    mark = 2
                elif j==0 and i!=N-1:
                    i+=1
                    mark = 2
            elif mark == 2:
                if j!=M-1 and i!=0:
                    i-=1
                    j+=1
                elif j==M-1 and i==0:
                    i+=1
                    mark=1
                elif j!=M-1 and i==0:
                    j+=1
                    mark=1
                elif j==M-1 and i!=0:
                    i+=1
                    mark = 1
                
        ans.append(matrix[N-1][M-1])        
        return ans
                    
                
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
