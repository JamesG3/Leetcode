class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        # initialize maxSave, using the first nut in nuts
        # if there is only one nut, squirrel has to reach the nut first, then go back to tree, even if the total distance is larger than double distance between nut and tree
        nut = nuts[0]                   
        dis_move = (abs(tree[0] - nut[0]) + abs(tree[1] - nut[1]))
        s_move = (abs(nut[0]-squirrel[0]) + abs(nut[1]-squirrel[1]) + abs(nut[0]-tree[0]) + abs(nut[1]-tree[1]))
        maxSave = dis_move*2 - s_move
        
        totalMove = 0
        
        # find the nut with max saving on distance, make it as the first nut to reach
        for i in xrange(len(nuts)):
            nut = nuts[i]
            s_move = (abs(nut[0]-squirrel[0]) + abs(nut[1]-squirrel[1]) + abs(nut[0]-tree[0]) + abs(nut[1]-tree[1]))
            dis_move = (abs(tree[0] - nut[0]) + abs(tree[1] - nut[1]))
            totalMove += dis_move * 2
            maxSave = max(maxSave, dis_move*2 - s_move)

        
        return totalMove - maxSave                
                
            
            
        
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        
        # There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. 
        # Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. 
        # The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell.
        # The distance is represented by the number of moves.
