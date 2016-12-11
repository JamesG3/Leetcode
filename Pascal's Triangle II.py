class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        ans=[1,1]
        tem=[1]
        count=0
        
        while rowIndex != 1:
            while count<len(ans)-1:
                tem.append(ans[count]+ans[count+1])
                count+=1
            tem.append(1)
            ans=tem
            tem=[1]         #reset tem
            count=0         #reset count
            rowIndex-=1
            
        return ans
        
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        #Given an index k, return the kth row of the Pascal's triangle.
        #For example, given k = 3,
        #Return [1,3,3,1].
