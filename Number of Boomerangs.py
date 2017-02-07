class Solution(object):
    def numberOfBoomerangs(self, points):
        length = len(points)
        distances = []
        for i in xrange(length):                #for every point in points
            rest = points[:i] + points[i+1:]    #rest part of points
            dic = {}
            for point in rest:                  #calculate the distance from the current point to every other point
                dis = self.distance(points[i], point)
                if dis not in dic:              #save the distance into dictionary
                    dic[dis] = 1
                else:
                    dic[dis] += 1
            distances.append(dic)
            
        counter = 0
        for dic in distances:                   #for every point's distance set
            for n in dic:                       #calculate the number of combinations for each distance
                if dic[n] != 1:
                    counter += dic[n] * (dic[n]-1)      #(first+end)*numbers/2
                    
        return counter
                
        
    def distance(self, A, B):
        return (A[0] - B[0])**2 + (A[1] - B[1])**2
        
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        #Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
        #Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
