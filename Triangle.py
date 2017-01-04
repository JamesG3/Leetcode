class Solution(object):
    def minimumTotal(self, triangle):
        y=0
        length=len(triangle)
        
        while y != length-1:                    #calculate sum from top to down
            for i in range(len(triangle[y])):
                if i == 0:                      #there is only one option for the first number of every line
                    triangle[y+1][0] += triangle[y][0]
                    
                if i == len(triangle[y])-1:     #same only one option for the last number
                    triangle[y+1][-1] += triangle[y][-1]
                    
                if i != len(triangle[y])-1 and y != 0:  #choose the smaller one for every two adjacent numbers
                    triangle[y+1][i+1] += min(triangle[y][i], triangle[y][i+1])
            y += 1
            
        return min(triangle[-1])
                    
            
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        
        #Given a triangle, find the minimum path sum from top to bottom. 
        #Each step you may move to adjacent numbers on the row below.
        #For example:[
        # [2],
        #[3,4],
       #[6,5,7],
      #[4,1,8,3]]
      #The minimum path sum from top to bottom is 11 (2 + 3 + 5 + 1 = 11).
