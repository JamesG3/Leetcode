
class Solution(object):

    # backtracking solution, TLE on N=15
    def countArrangement(self, N):
        self.counter = 0
        
        def helper(N, visted, length):
            if length == N:
                self.counter += 1
                return
            for i in xrange(1, N+1):
                if visted[i-1]==0 and (i % (length+1)==0 or (length+1) % i == 0):
                    visted[i-1] = 1
                    helper(N, visted, length+1)
                    visted[i-1] = 0
                    
        helper(N, [0 for i in xrange(N)], 0)
        return self.counter
    
    
    
    
    
    
    def countArrangement(self, N):
        counter = 0
        queue = []
        x = []
        queue.append(x);
        while(len(queue) >0):
            x = queue.pop()
            if len(x) == N:     # counter+1 only if it satisfy the length
                counter+=1
            else:
                for i in xrange(1,N+1):
                    current = x[:]
                    if i not in current:
                        if (i % (len(current)+1) == 0) or ((len(current)+1) % i == 0):      
                            # add one more number at the end of current list, append this list in the queue
                            # if there is no more number to append (from 1 to N), then ignore this current list
                            current.append(i)
                            queue.append(current)
                            
        return counter
        
    
        """
        :type N: int
        :rtype: int
        """
        
        # Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 ≤ i ≤ N) in this array:

        # The number at the ith position is divisible by i.
        # i is divisible by the number at the ith position.
        # Now given N, how many beautiful arrangements can you construct? 
