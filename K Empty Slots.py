class Solution(object):
    
    # sliding window solution
    def kEmptySlots(self, flowers, k):
        length = len(flowers)
        flopos = [0 for i in xrange(length)]
        
        for i in xrange(length):                    # transfer -> index: the position of flowers, flopos[index]: blooming day
            flopos[flowers[i]-1] = i+1

        res = float('Inf')        
        i, j = 0, k+1                       # left and right index for sliding window
        while j<length:
            if not (flopos[i] < res and flopos[j] < res):       # pass flowers whose days are larger than current answer
                j+=1
                i+=1
                continue
            
            flag = 0
            for m in xrange(i+1, j):
                if flopos[m] < flopos[i] or flopos[m] < flopos[j]:
                    flag = 1
                    break
            if flag == 0:    
                res = min(res, max(flopos[i], flopos[j]))
            j+=1
            i+=1
        
        if res != float('Inf'):
            return res
        return -1
        
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
        
