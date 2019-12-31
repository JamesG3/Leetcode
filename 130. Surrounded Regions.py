class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        captured = []
        visted = set()
        
        height = len(board)
        if not height:
            return board
        
        width = len(board[0])
        if not width:
            return board
        
        for x in range(height):
            for y in range(width):
                element = board[x][y]
                if (element != 'O') or ((x, y) in visted):
                    continue
                    
                stack = [[x, y]]
                visted.add((x, y))
                cur_visted = set([(x, y)])
                # DFS get all neighbors of the current 'O'
                while stack:
                    tmp_x, tmp_y = stack.pop()
                    for nei_x, nei_y in [[tmp_x, tmp_y+1], [tmp_x, tmp_y-1], [tmp_x+1, tmp_y], [tmp_x-1, tmp_y]]:
                        if nei_x in (height, -1) or \
                            nei_y in (width, -1) or \
                            board[nei_x][nei_y] == 'X' or \
                            (nei_x, nei_y) in cur_visted:
                            continue
                            
                        cur_visted.add((nei_x, nei_y))
                        visted.add((nei_x, nei_y))
                        stack.append([nei_x, nei_y])
                
                # traverse all points, check if captured
                capture_flag = 1
                for m, n in cur_visted:
                    if m in (0, height-1) or n in (0, width-1):
                        capture_flag = 0
                        break
                if capture_flag == 1:
                    for m, n in cur_visted:
                        captured.append([m, n])
        # update all the captured points           
        for m, n in captured:
            board[m][n] = 'X'
            
        return board
                        
'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Solution: DFS, hashtable, Stack
Time, Space: O(n)
'''          
    
