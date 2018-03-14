class Solution(object):
    def lengthLongestPath(self, input):
        paths = input.split('\n')
        pathlength = {0: 0}
        mxlen = 0
        
        for path in paths:
            path1 = path.lstrip('\t')
            depth = len(path) - len(path1)            
            if '.' in path1:
                mxlen = max(mxlen, pathlength[depth]+len(path1))
            else:
                pathlength[depth+1] = pathlength[depth] + len(path1) + 1
                
        return mxlen
                
                   
        
        """
        :type input: str
        :rtype: int
        """
        
