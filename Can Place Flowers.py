class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        counter = 0
        L = []
        
        flowerbed = [1,0] + flowerbed + [0,1]
        
        for i in xrange(len(flowerbed)):
            if flowerbed[i]==1:
                if counter > 1:
                    L.append(counter)
                counter = 0
            else:
                counter+=1
        if counter > 1:
            L.append(counter)

        for item in L:
            n -= (item-1)/2
            if n <= 0:
                return True
        
        
        if n<=0:
            return True
        else:
            return False
                
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        #Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
        #However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
        #Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
