class Solution(object):
    def lastRemaining(self, n):
        
        jump=2
        start=1
        end=n
        status=0
        
        while start != end:                 #until one element left
            if status == 0:
                if (end-start)%jump==0:     #whether to change the last element
                    end-=jump/2
                start+=jump/2
                status=1
            else:
                if (end-start)%jump==0:     #whether to change the first element
                    start+=jump/2
                end-=jump/2
                status=0
            jump*=2                         #double the jump
            
        return start
        
        
        
        #Time exceeded version
        
        #l=range(1,n+1)
        #status=0
        #while len(l)!=1:
        #    if status==0:
        #        n=0
        #        while n < len(l):
        #            del l[n]
        #            n+=1
        #        status=1
                
        #    else:
        #        n=-1
        #        while n >= -len(l):
        #            del l[n]
        #            n-=1
        #        status=0
                
        #return l[0]
        
        """
        :type n: int
        :rtype: int
        """
        
