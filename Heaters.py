class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        i = 0       # i is the index of houses
        j = 0       # j in the index of heaters
        
        house_range = len(houses)
        heaters_range = len(heaters)
        
        radius = 0          #initialize the radius range
        temdistance = 10**9     #set the temdistance to max value
        
        while i < house_range and j < heaters_range:        #traverse houses and heaters
            currentdistance = abs(heaters[j]-houses[i])
            
            if currentdistance < temdistance:       #update the temdistance, to find the nearest heater for every house
                temdistance = currentdistance
                j += 1
                
            elif currentdistance == temdistance:    #update the radius using larger one between former radius and currentdis
                radius = max(radius, currentdistance)
                i += 1                              #move to the next house
                temdistance = 10**9         #reset temdistance
            else:                                   #if currentdistance is getting larger
                radius = max(radius, abs(heaters[j-1]-houses[i]))       #then using former heater to calculate
                j -= 1                      #back to the former heater
                i += 1                      #move to the next house
                temdistance = 10**9         #reset temdistance
                
        if j == heaters_range:  #if the loop is ended by heaters, then check the distence between furthest house and the last heater
            radius = max(radius, abs(heaters[-1]-houses[-1]), currentdistance)
            
        return radius
        
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
      #Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
      #Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
      #So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.
