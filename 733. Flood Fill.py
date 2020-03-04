class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        
        height = len(image)
        if not height:
            return image
        width = len(image[0])
        if not width:
            return image
        
        bfs = [[sr, sc]]
        visted = set([(sr, sc)])
        old_color = image[sr][sc]
        
        while bfs:
            tmp_bfs = []
            for x, y in bfs:
                image[x][y] = newColor
                for i, j in dirs:
                    new_x, new_y = x + i, y + j
                    if (0 <= new_x < height) and (0<= new_y < width) and image[new_x][new_y] == old_color and (new_x, new_y) not in visted:
                        tmp_bfs.append([new_x, new_y])
                        visted.add((new_x, new_y))
            bfs = tmp_bfs
        
        return image
    
'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.

Solution: BFS, hashtable
Time, Space: O(n)


'''
