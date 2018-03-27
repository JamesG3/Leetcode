class Solution(object):
    def canTransform(self, start, end):

        
        # consider X as space, all R can be moved to right, all L can be moved to left
        if not start.replace("X","")==end.replace("X",""):        # if sequence is messed up, then False
            return False
        
        length = len(start)
        i,j = 0,0
        flag = 0
        
        while i<length and j<length:
            if start[i] == "X":         # find next L or R
                i+=1
                continue

            if end[j] == "X":           # find next L or R
                j+=1
                continue
                    
            if start[i]==end[j]=="R":   # compare start and end
                if i>j:                 # if R moves left
                    return False
                i+=1
                j+=1
                
            elif start[i]==end[j]=="L":
                if i<j:                 # if L moves right
                    return False
                i+=1
                j+=1
            else:
                return False
        
        return True
        
        
        
        
        
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        
        # In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
        # a move consists of either replacing one occurrence of "XL" with "LX", 
        # or replacing one occurrence of "RX" with "XR". 
        # Given the starting string start and the ending string end, 
        # return True if and only if there exists a sequence of moves to transform one string to the other.
