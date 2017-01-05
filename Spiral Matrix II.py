class Solution(object):
    def generateMatrix(self, n):
        matrix=[]
        for i in xrange(n):
            matrix.append([0]*n)
        coordinateNum = n*n
        
        if len(matrix) == 0:
            return []
        return self.appen(matrix, [], coordinateNum, 0, 0, 0, 1)
        
        
        
        
    def appen(self, matrix, dic, coordinateNum, value, x, y, set ):
        if len(dic)<=coordinateNum:
            if set==1:
                #going right
                while([x,y] not in dic and x!=len(matrix[0]) and len(dic)!=coordinateNum):
                    value+=1
                    dic.append([x,y])
                    matrix[y][x] = value
                    x+=1
                if y+1 < len(matrix) and [x-1,y+1] not in dic:
                    self.appen(matrix, dic, coordinateNum, value, x-1, y+1, 2)
                    
            elif set==2:
                #going down
                while([x,y] not in dic and len(dic)!=coordinateNum and y!=len(matrix)):
                    value+=1
                    dic.append([x,y])
                    matrix[y][x] = value
                    y+=1
                if x!=0 and [x-1,y-1] not in dic:
                    self.appen(matrix, dic, coordinateNum, value, x-1, y-1, 3)
                    
            elif set==3:
                #going left
                while([x,y] not in dic and len(dic)!=coordinateNum and x!=-1):
                    value+=1
                    dic.append([x,y])
                    matrix[y][x] = value
                    x-=1
                if [x+1,y-1] not in dic:
                    self.appen(matrix, dic, coordinateNum, value, x+1, y-1, 4)
                    
            elif set==4:
                #going up
                while([x,y] not in dic and len(dic)!=coordinateNum):
                    value+=1
                    dic.append([x,y])
                    matrix[y][x] = value
                    y-=1
                if [x+1,y+1] not in dic:
                    self.appen(matrix, dic, coordinateNum, value, x+1, y+1, 1)

        return matrix
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        #Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
        #For example,
        #Given n = 3,
        #You should return the following matrix:
        #[[ 1, 2, 3 ],
        #[ 8, 9, 4 ],
        #[ 7, 6, 5 ]]
