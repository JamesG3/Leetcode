class Solution(object):
    def numberOfArithmeticSlices(self, A):
        if len(A)<3:
            return 0
        
        num=0
        count=2                                             #counter. used for calculations
        difference=A[1]-A[0]                                #initialize the difference
        
        for n in range(2,len(A)):
            if A[n]-A[n-1]==difference:
                count+=1
            else:
                if count>=3:
                    num += (count-2)*(count-1)/2            #calculate the nth of 1,3,6,10... use formula nth=n(n-1)/2
                count=2                                     #reset counter
                difference=A[n]-A[n-1]                      #reset difference
       
        if count>=3:
            num += (count-2)*(count-1)/2
            
        return num
                
        """
        :type A: List[int]
        :rtype: int
        """
