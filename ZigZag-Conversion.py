class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows == 1:
            return s
        res = []
        offset = 0
        
        tmp = []
        cur_len = 0
        for i in s:
            if offset == 0 or offset % (numRows-1) == 0:
                tmp.append(i)
                cur_len += 1
                
                if cur_len == numRows:
                    res.append(tmp)
                    offset += 1
                    cur_len = 0
                    tmp = []
                    continue
                
            else:
                spaceNum = offset % (numRows-1)
                res.append((numRows-1-spaceNum) * [''] + [i] + spaceNum * [''])
                offset += 1
                
        if tmp:
            res.append(tmp + [''] * (numRows-cur_len))
            

        # construct the output string
        output_string = []

        for y in xrange(len(res[0])):
            for x in xrange(len(res)):
                if res[x][y]:
                    output_string.append(res[x][y])
        return ''.join(output_string)
    
    
    
   '''
   Using offset as condition to figure out which column
   Using offset to control the zigzag format
   Construct a zigzag list, then traverse in different direction, construct a new string
   '''
