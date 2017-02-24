class Solution(object):
    def bulbSwitch(self, n):
        
        return int(math.sqrt(n))
        
        """
        #brute force
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        bulbs = [1]*n
        
        mid = n/2
        
        m = 2
        i = 1
        while m <= mid:
            j = i
            while j<n:
                if bulbs[j] == 1:
                    bulbs[j] = 0
                else:
                    bulbs[j] = 1
                j+=m
            m+=1
            i+=1
            #print bulbs
            

        return bulbs[:mid].count(1) + bulbs[mid:].count(0)
        
        
            
        """
        
        """
        :type n: int
        :rtype: int
        """
        
        
        #There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. 
        #On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
        #For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
        #Find how many bulbs are on after n rounds.
