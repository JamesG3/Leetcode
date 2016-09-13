class Solution(object):
    def generate(self, numRows):
        r=[[1],[1,1]]
        num=[1,1]
        count=0
        if numRows==0:
            r=[]
            return r
        if numRows==1:
            r=[[1]]
            return r
        if numRows==2:
            r=[[1],[1,1]]
            return r
        else:
            tem=[1]
            while numRows!=2:
                while count<len(num)-1:
                    tem.append(num[count]+num[count+1])
                    count+=1
                tem.append(1)
                num=tem
                r.append(num)
                tem=[1]
                count=0
                numRows-=1
            
        return r
            
        """
        :type numRows: int
        :rtype: List[List[int]]
        Given numRows, generate the first numRows of Pascal's triangle.
        """
