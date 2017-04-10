class Solution(object):
    def leastBricks(self, wall):
        
        dic = {}
        S = sum(wall[0])
        for line in wall:
            if line[0] in dic:
                dic[line[0]]+=1
            else:
                dic[line[0]] = 1
            for i in xrange(1, len(line)):
                line[i] += line[i-1]
                if line[i] in dic:
                    dic[line[i]]+=1
                else:
                    dic[line[i]] = 1
        ans = 0
        for item in dic:
            if item != S:
                ans = max(ans, dic[item])
        return len(wall)-ans
        
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        
        #There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. 
        #The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
