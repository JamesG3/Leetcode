class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        self.A = A
        self.B = B
        
        check_a = self.check(A[0])
        check_b = self.check(B[0])
        if check_a == check_b == -1:
            return -1
        
        if check_a == -1:
            return check_b
        elif check_b == -1:
            return check_a
        else:
            return min(check_a, check_b)
        
    def check(self, x):
        a_count = b_count = 0
        for i in range(len(self.A)):
            if x not in (self.B[i], self.A[i]):
                return -1
            if x != self.B[i]:
                b_count += 1
            elif x != self.A[i]:
                a_count += 1
        return min(a_count, b_count)
            

        
'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the i-th domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
If it cannot be done, return -1.

Solution: Greedy, traverse list
Time: O(n)
Space: O(1)
'''
        
                
            
