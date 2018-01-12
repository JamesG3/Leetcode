class Solution(object):
    def findLonelyPixel(self, picture):
        coor = []
        row = {}
        col = {}
        
        n = len(picture)
        m = len(picture[0])
        
        for i in xrange(n):                 # store coordinate for each pixel 'B'
            for j in xrange(m):
                if picture[i][j] == 'B':
                    coor.append([i, j])
                    if i not in row:        # for all pixel 'B', count the number of x-coordinate and y-coordinate
                        row[i] = 1
                    else:
                        row[i] += 1
                    
                    if j not in col:
                        col[j] = 1
                    else:
                        col[j] += 1
        
        counter = 0
        for c in coor:      # traverse each cached coordinate, check whether both x-coordinate and y-coordinate appear once
            if row[c[0]] == col[c[1]] == 1:
                counter += 1
        return counter
            
                        
                    
        
        
        
        
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        # Given a picture consisting of black and white pixels, find the number of black lonely pixels.
        # The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
        # A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
