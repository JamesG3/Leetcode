class Solution(object):
    def isValidSudoku(self, board):                 #brute force
        orig = ['1','2','3','4','5','6','7','8','9','0']
        compare = copy.deepcopy(orig)
        index = len(board)
        
        for line in board:                  #check every row
            for n in line:
                if n != '.':
                    if n in compare:
                        compare.remove(n)
                    else:
                        return False
            
            compare = copy.deepcopy(orig)
        
        compare = copy.deepcopy(orig)
            
        for j in xrange(index):             #check every column
            for i in xrange(index):
                if board[i][j] != ".":
                    if board[i][j] in compare:
                        compare.remove(board[i][j])
                    else:
                        return False
            print compare
            compare = copy.deepcopy(orig)
        
        compare = copy.deepcopy(orig)
        i = 0
        j = 0
        jmark = j
        imark = i
        
        while i != index:               #check every 9*9 unit
            if j==index and (i+1)%3==0:
                j=0
                jmark=j
                i+=1
                imark=i
                compare=copy.deepcopy(orig)
                continue
            
            if j==index and (i+1)%3!=0:
                j=jmark
                i+=1
                
            if j != jmark and j%3 == 0 and (i+1)%3!=0:
                i+=1
                j=jmark
                
            if j != jmark and j%3 == 0 and (i+1)%3==0:
                jmark=j
                i=imark
                compare=copy.deepcopy(orig)
                
            if board[i][j] != '.':
                
                if board[i][j] in compare:
                    compare.remove(board[i][j])
                else:
                    return False
            j+=1
                    
 
        return True

                    
            
        
        """
        :type board: List[List[str]]
        :rtype: bool
        """
