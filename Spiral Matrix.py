class Solution(object):                         #using recursive, status code to decide the going direction
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        coordinateNum = len(matrix)*len(matrix[0])
        return self.appen(matrix, [], coordinateNum, [], 0, 0, 1)
        
        
    def appen(self, matrix, dic, coordinateNum, result, x, y, set ):
        if len(dic)<=coordinateNum:
            if set==1:
                #going right
                while([x,y] not in dic and x!=len(matrix[0]) and len(dic)!=coordinateNum):
                    dic.append([x,y])
                    result.append(matrix[y][x])
                    x+=1
                if y+1 < len(matrix) and [x-1,y+1] not in dic:
                    self.appen(matrix, dic, coordinateNum, result, x-1, y+1, 2)
                    
            elif set==2:
                #going down
                while([x,y] not in dic and len(dic)!=coordinateNum and y!=len(matrix)):
                    dic.append([x,y])
                    result.append(matrix[y][x])
                    y+=1
                if x!=0 and [x-1,y-1] not in dic:
                    self.appen(matrix, dic, coordinateNum, result, x-1, y-1, 3)
                    
            elif set==3:
                #going left
                while([x,y] not in dic and len(dic)!=coordinateNum and x!=-1):
                    dic.append([x,y])
                    result.append(matrix[y][x])
                    x-=1
                if [x+1,y-1] not in dic:
                    self.appen(matrix, dic, coordinateNum, result, x+1, y-1, 4)
                    
            elif set==4:
                #going up
                while([x,y] not in dic and len(dic)!=coordinateNum):
                    dic.append([x,y])
                    result.append(matrix[y][x])
                    y-=1
                if [x+1,y+1] not in dic:
                    self.appen(matrix, dic, coordinateNum, result, x+1, y+1, 1)

        return result
            
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        Should return [1,2,3,6,9,8,7,4,5]
        """
        
