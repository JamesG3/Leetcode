class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        All= (C- A)* (D- B)+ (G- E)* (H- F)
        Le = max(0,min(C,G)- max(A,E))
        Hi = max(0,min(D,H)- max(B,F))

        return All- Le* Hi      
       
       
       #Find the total area covered by two rectilinear rectangles in a 2D plane.
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
